from django.urls import path 
from . import views
from django.contrib.auth import views as v

urlpatterns = [
    path('accounts/login/', v.LoginView.as_view(), name='login'),
    path('accounts/logout/', v.LogoutView.as_view(next_page='/'), name='logout'),
    path('', views.home, name='home'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/new/', views.newBook, name='newBook'),
    path('book/', views.book_list, name='book_list'),
]