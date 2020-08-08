from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    gid = models.CharField(max_length=300)
    started = models.DateField(null=True)
    finished = models.DateField(null=True)


class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    readinglist = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='read_by')
    image = models.ImageField(default='static/reading/resources/image_placeholder.png')


class Comment(models.Model):
    pass


class Post(models.Model):
    pass
