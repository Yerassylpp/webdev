from django.urls import path
from .models import *
from api import views

urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_one),
    path('category/', views.category_list),
    path('category/<int:id>/', views.category_one),
]