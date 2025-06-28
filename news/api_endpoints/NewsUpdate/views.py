from rest_framework import generics, permissions
from news.models import News
from news.api_endpoints.NewsUpdate.serializer import NewsUpdateSerializer

class NewsUpdateView(generics.UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]