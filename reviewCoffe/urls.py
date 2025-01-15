from django.urls import path
from . import views

urlpatterns = [
    path('reviewcoffe/', views.reviewCoffeCreateListView.as_view(), name='reviewcoffe-list-create'),
    path('reviewcoffe/<int:pk>/', views.reviewCoffeRetrieveUpdateDestroyView.as_view(), name='reviewcoffe-detail'),
]
