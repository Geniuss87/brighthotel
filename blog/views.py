
from django.views import generic

from blog.models import Blog


class BlogView(generic.ListView):
    model = Blog
    template_name = "blog.html"
    context_object_name = "blog"

    def get_queryset(self):
        queryset = Blog.objects.all().order_by('id')
        return queryset


class BlogSingleView(generic.DetailView):
    model = Blog
    template_name = "blog-single.html"
    context_object_name = "post"
