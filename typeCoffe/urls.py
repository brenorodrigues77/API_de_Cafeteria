from django.urls import path
from . import views

urlpatterns = [
    path('typecoffe/', views.TypeCoffeCreateListView.as_view(), name='typecoffe-list-create'),
    path('typecoffe/<int:pk>/', views.TypeCoffeRetrieveUpdateDestroyView.as_view(), name='typecoffe-detail'),
]