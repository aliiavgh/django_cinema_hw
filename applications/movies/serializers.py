from django.contrib.auth import get_user_model
from rest_framework import serializers

from applications.movies.models import Movie, Rating
from applications.movies import services as likes_services

User = get_user_model()


class RatingSerializer(serializers.ModelSerializer):
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
