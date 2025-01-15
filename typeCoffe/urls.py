from django.urls import path
from . import views

urlpatterns = [
    path('typecoffe/', views.typeCoffeCreateListView.as_view(), name='typecoffe-list-create'),
    path('typecoffe/<int:pk>/', views.typeCoffeRetrieveUpdateDestroyView.as_view(), name='typecoffe-detail'),
]