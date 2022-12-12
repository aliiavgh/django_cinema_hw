from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.movies.views import MovieApiView, RatingApiView

router = DefaultRouter()
router.register('', MovieApiView)

urlpatterns = []
urlpatterns += router.urls
