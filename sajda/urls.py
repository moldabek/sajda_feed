from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import RegisterView, FeedView, FeedListView

urlpatterns = [
    # separate to avoid conflicts with other apps
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title='Sajda API', description='API for Sajda app')),
    path('feed/', FeedListView.as_view(), name='feed_list'),
    path('feed/<int:pk>/', FeedView.as_view(), name='feed_detail'),
]
