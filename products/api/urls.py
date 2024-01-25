from django.urls import path
from . import views

urlpatterns = [
    path('product/add/', views.ProductAddView.as_view(), name="product_create" )
]
