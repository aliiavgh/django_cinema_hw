from django.contrib import admin

from applications.movies.models import Movie, Likes, Rating

admin.site.register(Movie)
admin.site.register(Likes)
admin.site.register(Rating)
