from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken

from .models import Card
from .serializers import RegisterSerializer, FeedSerializer, FeedInteractionSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CustomPagination(CursorPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
    ordering = '-created_at'


def get_user_from_token(token) -> User:
    token = AccessToken(token)
    token.verify()
    user = JWTAuthentication().get_user(token)
    return user


class FeedView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = FeedSerializer

    def get(self, request, pk: int, *args, **kwargs):  # noqa
        card = get_object_or_404(Card, id=pk)
        serializer = self.serializer_class(card)
        return Response(serializer.data)

    def post(self, request, pk: int, *args, **kwargs):  # noqa
        serializer = FeedInteractionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = get_user_from_token(request.headers.get('Authorization'))
        except Exception as e:
            return Response({'status': 'error', 'message': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        card = get_object_or_404(Card, id=pk, active=True)
        card.add_interaction(serializer.validated_data['interaction_type'], user)
        card.save()
        return Response({'status': 'success', 'message': 'Interaction added successfully'})


class FeedListView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):  # noqa
        cards = Card.objects.filter(active=True)
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(cards, request)
        new_result_page = []
        if token := request.headers.get('Authorization'):
            try:
                user = get_user_from_token(token)
            except Exception as e:
                return Response({'status': 'error', 'message': str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
            for card in result_page:
                if not card.card_hidden(user):
                    card.set_user_interactions(user)
                    new_result_page.append(card)
        serializer = FeedSerializer(new_result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class FeedInteractionView(APIView):
    permission_classes = (AllowAny,)
