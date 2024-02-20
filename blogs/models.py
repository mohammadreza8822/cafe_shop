from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from ckeditor.fields import RichTextField


class Blog(models.Model):
    STATUS = (
    (0,"Draft"),
    (1,"Publish")
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    description = RichTextField()
    description2 = RichTextField()
    tips = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    author_note = models.TextField()

    image_cover = models.ImageField(upload_to='blog_covers/', blank=True)
    image_detail = models.ImageField(upload_to='blog_covers/', blank=True)
    image_detail2 = models.ImageField(upload_to='blog_covers/', blank=True)
    image_detail3 = models.ImageField(upload_to='blog_covers/', blank=True)

    datetime_created = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    datetime_commented = models.DateTimeField(auto_now_add=True)
    phone_number = models.IntegerField(max_length=10)
    email = models.EmailField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.author} on '{self.blog}'"