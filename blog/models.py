from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Blog(models.Model):
    title = models.CharField(max_length=150, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="blog")
    text = models.TextField()

    def __str__(self):
        return f'{self.title}'


# class Image(models.Model):
#     image = models.ImageField(upload_to="blog")
#     post = models.ForeignKey(Blog,
#                              on_delete=models.CASCADE,
#                              related_name="images")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True, null=True)

