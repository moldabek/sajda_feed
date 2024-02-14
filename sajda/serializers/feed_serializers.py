from rest_framework import serializers

from sajda.models import Card, UserCardInteraction


class FeedSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField()

    class Meta:
        model = Card
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if hasattr(instance, 'liked'):
            data['liked'] = instance.liked
        if hasattr(instance, 'dhikrs_count'):
            data['dhikrs_count'] = instance.dhikrs_count
        return data


class FeedInteractionSerializer(serializers.ModelSerializer):
    interaction_type = serializers.ChoiceField(choices=UserCardInteraction.INTERACTION_TYPE, required=True)

    class Meta:
        model = UserCardInteraction
        fields = ('interaction_type',)
