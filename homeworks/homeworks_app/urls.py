from django.urls import path
from . import views
from .views import client_ordered_products

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('client/<int:client_id>/ordered_products/', client_ordered_products, name='client_ordered_products')
]