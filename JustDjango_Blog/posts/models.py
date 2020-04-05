from django.urls import reverse
from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# a user model
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


# create a model to allow us categorize each post based on specific category
class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# the post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = HTMLField()
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)

    # each post must have one author, but an author could have multiple posts
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()

    # each post could have multiple categories, and each category could be applied to multiple posts
    categories = models.ManyToManyField(Category)

    previous_post = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, related_name='previous')
    next_post = models.ForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, related_name='next')

    # if true render the post
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={
            'post_id': self.id,
        })
