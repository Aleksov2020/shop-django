from django.urls import path

import api.views

urlpatterns = [
    path('categories/', api.views.CategoryListCreateAPIView.as_view()),
    path('categories/<int:pk>/', api.views.CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('items/', api.views.ItemListCreateAPIView.as_view()),
    path('items/<int:pk>/', api.views.ItemRetrieveUpdateDestroyAPIView.as_view()),
]
