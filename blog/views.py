from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'blog/home.html')