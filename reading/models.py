from django.db import models
from django.contrib.auth.models import AbstractUser


class Book(models.Model):
    title = models.CharField(max_length=100)
    synopsis = models.TextField()

    CATEGORIES = [
        ('0', 'Arts & Music'),
        ('1', 'Biographies'),
        ('2', 'Business'),
        ('3', 'Comics'),
        ('4', 'Computers & Tech'),
        ('5', 'Cooking'),
        ('6', 'Education & Reference'),
        ('7', 'Entertainment'),
        ('8', 'Health & Fitness'),
        ('9', 'History'),
        ('10', 'Hobbies & Crafts'),
        ('11', 'Home & Garden'),
        ('12', 'Horror'),
        ('13', 'Kids'),
        ('14', 'Literature & Fiction'),
        ('15', 'Medical'),
        ('16', 'Mysteries'),
        ('17', 'Parenting'),
        ('18', 'Spirituality'),
        ('19', 'Romance'),
        ('20', 'Sci-Fi & Fantasy'),
        ('21', 'Science & Math'),
        ('22', 'Self-Help'),
        ('23', 'Social Sciences'),
        ('24', 'Sports'),
        ('25', 'Travel'),
        ('26', 'Crime')
    ]

    category = models.CharField(max_length=2, choices=CATEGORIES)
    image = models.CharField(max_length=200)


class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    reading = models.ManyToManyField(Book, related_name='reading')
    saved = models.ManyToManyField(Book, related_name='saved')
    read = models.ManyToManyField(Book, related_name='read')


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    books = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='author')
    image = models.CharField(max_length=200)


class Comment(models.Model):
    pass

class Post(models.Model):
    pass