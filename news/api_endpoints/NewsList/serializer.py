from rest_framework import serializers
from news.models import News

class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'slug', 'is_active', 'views_count']