from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment

class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['title', 'author', 'categories', 'created']
    search_fields = ['title', 'author__username', 'content']
    list_filter = ['categories', 'tags']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
