from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/add/', views.create_review, name='create_review'),
]
