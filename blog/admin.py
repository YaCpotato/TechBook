from django.contrib import admin

# Register your models here.


from .models import Book,Review,Image

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Image)