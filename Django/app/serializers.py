from app.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeList


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag