from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()


class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    reading = models.ManyToManyField(Book, related_name='reading')
    saved = models.ManyToManyField(Book, related_name='saved')
    read = models.ManyToManyField(Book, related_name='read')


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='author')


class Comment(models.Model):
    pass

class Post(models.Model):
    pass