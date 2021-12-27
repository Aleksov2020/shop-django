from django.urls import path
from shop import views

urlpatterns = [
    path('', views.index),

    path('categories/', views.categories_list),
    path('categories/<int:category_id>/', views.item_list),
    path('items/<int:item_id>/', views.item_details),
]
