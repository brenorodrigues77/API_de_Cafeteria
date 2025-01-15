from django.urls import path
from . import views

urlpatterns = [
    path('companycoffe/', views.companyCoffeCreateListView.as_view(), name='companycoffe-list-create'),
    path('companycoffe/<int:pk>/', views.companyCoffeRetrieveUpdateDestroyView.as_view(), name='companycoffe-detail'),
]