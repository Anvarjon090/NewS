from rest_framework import generics, permissions
from news.models import News, Comment, MediaFile
from news.api_endpoints.NewsCreate.serializer import *


class NewsCreateView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)