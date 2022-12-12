from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, required=True)
    password_confirm = serializers.CharField(min_length=6, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.get('password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('Passwords do not match!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
