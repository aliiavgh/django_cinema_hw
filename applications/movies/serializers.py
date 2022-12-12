from django.contrib.auth import get_user_model
from rest_framework import serializers

from applications.movies.models import Movie, Rating
from applications.movies import services as likes_services

User = get_user_model()


class FanSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class RatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""
    class Meta:
        model = Rating
        fields = ("star", "movie")

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            movie=validated_data.get('movie', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'total_likes', 'rating')

    def get_is_fan(self, obj) -> bool:
        """Check if a `request.user` has liked this tweet (`obj`).
        """
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)
