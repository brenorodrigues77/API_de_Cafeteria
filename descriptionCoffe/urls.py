from django.urls import path
from . import views

urlpatterns = [
    path('descriptioncoffe/', views.descriptionCoffeCreateListView.as_view(), name='descriptioncoffe-list-create'),
    path('descriptioncoffe/<int:pk>/', views.descriptionRetrieveUpdateDestroyView.as_view(), name='descriptioncoffe-detail'),
]
