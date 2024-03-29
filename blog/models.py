from django.db import models
from django.utils import timezone

class Book(models.Model):
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images',blank=True, null=True)
    title = models.CharField(max_length=32)
    link = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Review(models.Model):
    book = models.ForeignKey('blog.Book', on_delete=models.CASCADE, related_name='reviews',blank=True, null=True)
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField()
    star = models.IntegerField()