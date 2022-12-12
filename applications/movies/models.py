from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()


class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    likes = GenericRelation(Likes)

    def __str__(self):
        return self.title

    @property
    def total_likes(self):
        return self.likes.count()


class Rating(models.Model):
    ip = models.CharField(max_length=15)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Rating(models.Model):
    RATE_CHOICES = (
        (1, 'Bad'),
        (2, 'Ok'),
        (3, 'Fine'),
        (4, 'Good'),
        (5, 'Amazing')
    )
    star = models.PositiveIntegerField(choices=RATE_CHOICES)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="rating")

    def __str__(self):
        return f"{self.star} - {self.movie}"
