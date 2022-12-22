from django.urls import reverse_lazy
from django.views import generic
from blog.forms import CommentForm
from blog.models import Blog, Comment


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     form = CommentForm()
    #     context['form'] = form
    #     print(context)
    #     return context
    #


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog-single.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user

        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        blog_id = self.object.post.id
        return reverse_lazy('blog_single', args=(blog_id,))
