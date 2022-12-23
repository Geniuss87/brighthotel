from django import forms

from blog.models import Comment, Blog


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'image']

    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control px-3 py-3'})
        self.fields['text'].widget.attrs.update({'class': 'form-control px-3 py-3'})


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text', 'post']


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'image']

    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control px-3 py-3'})
        self.fields['text'].widget.attrs.update({'class': 'form-control px-3 py-3'})

