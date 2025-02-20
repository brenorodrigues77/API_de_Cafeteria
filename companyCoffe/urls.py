from django.urls import path
from . import views

urlpatterns = [
    path('companycoffe/', views.CompanyCoffeCreateListView.as_view(),
         name='companycoffe-list-create'),
    path('companycoffe/<int:pk>/', views.CompanyCoffeRetrieveUpdateDestroyView.as_view(),
         name='companycoffe-detail'),
    path('companycoffe/stats/', views.CompanyCoffeStatsView.as_view(),
         name='companycoffe-stats-view'),
]
