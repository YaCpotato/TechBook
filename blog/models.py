from django.db import models
from django.utils import timezone

class Book(models.Model):
    #author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    link = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Review(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    star = models.IntegerField()

class Image(models.Model):
    image = models.ImageField(upload_to='images')