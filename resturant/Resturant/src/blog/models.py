from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    tags = TaggableManager(blank=True)
    categories = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
