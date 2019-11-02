from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# adding custom manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # set title column for the post table
    title = models.CharField(max_length=250)

    # slug is a short label intended for URLS
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # Define a many to one relationship
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')

    # set the post body column for the post table
    body = models.TextField()

    # when the post was published
    publish = models.DateTimeField(default=timezone.now)

    # when the post was created
    created = models.DateTimeField(auto_now_add=True)

    # the last time the post was updated
    updated = models.DateTimeField(auto_now=True)

    # set the status of the post depending on the STATUS_CHOICES parameter
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    # The default manager
    objects = models.Manager()

    # The custom manager
    published = PublishedManager()

    # tell django to sort posts in descending order relative to publication date
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
