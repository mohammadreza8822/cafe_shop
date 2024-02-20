from django.contrib import admin

from .models import Blog, Comment


class CommentsInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'phone_number']
    extra = 0

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'datetime_created']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [
        CommentsInline,
    ]


