from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:blog_id>/', views.edit_blog, name='edit_blog'),
]
