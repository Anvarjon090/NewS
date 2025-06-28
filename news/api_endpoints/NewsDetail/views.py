from rest_framework import generics, permissions
from news.models import News
from news.api_endpoints.NewsDetail.serializer import NewsDetailSerializer


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    permission_classes = [permissions.AllowAny]
