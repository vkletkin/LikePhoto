import imp
from pyexpat import model
from unicodedata import name
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_group')

    def __str__(self):
        return self.name[:100]


class Post(models.Model):
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_posts')
    group = models.ForeignKey(Group, on_delete=models.CASCADE,
                              related_name='group_posts', blank=True, null=True)
    rating = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    # def __str__(self):
    #   return self.image[:100]
