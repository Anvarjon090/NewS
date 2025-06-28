from rest_framework import generics, permissions
from news.models import News
from news.api_endpoints.NewsDelete.serializer import NewsDeleteSerializer


class NewsDeleteView(generics.DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]