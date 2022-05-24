from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>/add/', views.create_review, name='create_review'),
    path('<int:review_id>/edit/',
         views.edit_product_review, name='edit_product_review'),
    path('<int:review_id>/delete/',
         views.delete_product_review, name='delete_product_review'),
]
