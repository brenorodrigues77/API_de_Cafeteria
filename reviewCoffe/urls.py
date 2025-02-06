from django.urls import path
from . import views

urlpatterns = [
    path('reviewcoffe/', views.ReviewCoffeCreateListView.as_view(), name='reviewcoffe-list-create'),
    path('reviewcoffe/<int:pk>/', views.ReviewCoffeRetrieveUpdateDestroyView.as_view(), name='reviewcoffe-detail'),
]
