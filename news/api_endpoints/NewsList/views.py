from rest_framework import generics, permissions
from news.models import News
from news.api_endpoints.NewsList.serializer import NewsListSerializer

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    permission_classes = [permissions.AllowAny]