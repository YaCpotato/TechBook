from django.db import models

class Book(models.Model):
    Title = models.CharField(max_length=32)
    Link = models.CharField(max_length=200)

class Review(models.Model):
    Title = models.CharField(max_length=20)
    Content = models.TextField()
    Star = models.IntegerField()