# Generated by Django 4.1.4 on 2022-12-23 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_rename_room_image_post_alter_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='name',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
