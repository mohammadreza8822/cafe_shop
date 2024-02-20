from django.urls import path

from .views import BlogListView, blog_detail_view


urlpatterns = [
    path('list/', BlogListView.as_view(), name='blog_list'),
    path('<slug:slug>/', blog_detail_view, name='blog_detail'),
]