from django.urls import path
from news.api_endpoints import (
    NewsDetail,
    NewsUpdate,
    NewsList,
    NewsDelete,
    NewsCreate,
)

app_name = 'news'

urlpatterns = [
    path('news/', NewsList.NewsListView.as_view(), name='news-list'),
    path('news/create/', NewsCreate.NewsCreateView.as_view(), name='news-create'),
    path('news/<int:pk>/', NewsDetail.NewsDetailView.as_view(), name='news-detail'),
    path('news/<int:pk>/update/', NewsUpdate.NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete/', NewsDelete.NewsDeleteView.as_view(), name='news-delete'),
]