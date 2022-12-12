from django.shortcuts import render
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from applications.movies.mixins import LikedMixin
from applications.movies.models import Movie
from applications.movies.serializers import MovieSerializer, RatingSerializer


class RatingApiView(APIView):

    def post(self, request):
        serializer_class = RatingSerializer(data=request.data)
        serializer_class.is_valid()
        serializer_class.save()
        return Response(status=status.HTTP_201_CREATED)


class MovieApiView(LikedMixin, ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


