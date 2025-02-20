from django.urls import path
from . import views

urlpatterns = [
    path('descriptioncoffe/', views.DescriptionCoffeCreateListView.as_view(),
         name='descriptioncoffe-list-create'),
    path('descriptioncoffe/<int:pk>/', views.DescriptionRetrieveUpdateDestroyView.as_view(),
         name='descriptioncoffe-detail'),
]
