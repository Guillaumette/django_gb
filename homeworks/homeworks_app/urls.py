from django.urls import path
from . import views
from .views import client_ordered_products, upload_image, total_in_view, total_in_db, total_in_template

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('client/<int:client_id>/ordered_products/', client_ordered_products, name='client_ordered_products'),
    path('upload/', upload_image, name='upload_image'),
    path('db/', total_in_db, name='db'),
    path('view/', total_in_view, name='view'),
    path('template/', total_in_template, name='template'),
]