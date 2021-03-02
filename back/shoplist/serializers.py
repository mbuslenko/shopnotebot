from rest_framework import serializers
from .models import Profile, Item, Category


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['external_id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    profile = serializers.StringRelatedField(many=True)

    class Meta:
        model = Item
        fields = ['profile', 'name', 'link', 'price', 'month']
