from django.db import models
from common.models import User
from categories.models import Category
from tags.models import Tag

class MediaFile(models.Model):
    media_type = models.CharField(max_length=50)
    file = models.FileField(upload_to='media_files/')

    def __str__(self):
        return f"{self.media_type} - {self.file.name}"

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    categories = models.ManyToManyField(Category, related_name='news_ids')
    tags = models.ManyToManyField(Tag, related_name='news_ids')
    default_image = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True, blank=True, related_name='default_for_news')
    images = models.ManyToManyField(MediaFile, related_name='news_ids')
    is_active = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
    liked_by = models.ManyToManyField(User, related_name='liked_news', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"Comment by {self.user.email}"