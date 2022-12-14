from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .models import Likes

User = get_user_model()

def add_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    like, is_created = Likes.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user)
    return like

def remove_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    Likes.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()

