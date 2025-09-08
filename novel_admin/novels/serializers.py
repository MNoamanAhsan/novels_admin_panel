from rest_framework import serializers
from .models import Categoryn, Novels, Episode

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Episode
        fields=["id", "name", "text"]


class NovelSerializer(serializers.ModelSerializer):
    episodes=EpisodeSerializer(many=True, read_only=True)
    category_name=serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model=Novels
        fields=["id", "title", "auther", "summary", "image","category_name","episodes"]


class CategorySerializer(serializers.ModelSerializer):
    Novels=NovelSerializer(many=True, read_only=True)
    class Meta:
        model=Categoryn
        fields=["id","name","Novels"]