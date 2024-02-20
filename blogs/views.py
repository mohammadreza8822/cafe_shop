from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Blog, Comment
from .forms import CommentForm


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 6
    template_name = 'blogs/blog_list.html'
    context_object_name = 'blogs'
    def get_queryset(self):
        return Blog.objects.filter(status=1).order_by('-datetime_created')
        
    
def blog_detail_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog_comments = blog.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog = blog
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'blogs/blog_detail.html', {
        'blogs': blog,
        'comments': blog_comments,
        'comment_form': comment_form,
    })