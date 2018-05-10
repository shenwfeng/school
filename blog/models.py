from django.db import models
from django.utils.timezone import now

from django.contrib.auth.models import User
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,related_name='blog_posts',on_delete='CASCADE')
    body = models.TextField()
    publish = models.DateTimeField(default=now)
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    def __str__(self):
        return self.headline
    class Meta:
        ordering = ('headline',)
