from rest_framework import serializers
from news.models import News


class NewsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id']