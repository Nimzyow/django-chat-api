from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Notification


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Ensuring password is write-only

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        notification = Notification.objects.create(user=user)
        notification.save()
        return user
