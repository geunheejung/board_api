from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    family_name = models.CharField(max_length=30, blank=False)
    given_name = models.CharField(max_length=30, blank=False)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    updated_at = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.family_name + ' ' + self.given_name


class Post(models.Model):
    user_id = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    updated_at = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_id = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    updated_at = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.content

