from app.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializes a User object"""
    class Meta:
        model = User
        fields = ('id', 'username')


class AddressSerializer(serializers.ModelSerializer):
    """Serializes an Address object"""
    class Meta:
        model = Address

class RecipeSerializer(serializers.ModelSerializer):
    """Serializes a Recipe object"""
    class Meta:
        model = Recipe

class TagSerializer(serializers.ModelSerializer):
    """Serializes a Recipe object"""
    class Meta:
        model = Tag

class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Photo
        fields = ('url', 'id', 'photo')
        # owner = serializers.Field(source='owner.username')