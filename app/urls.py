from django.contrib import admin
from django.urls import path
from typeCoffe.views import typeCoffeCreateListView, typeCoffeRetrieveUpdateDestroyView
from descriptionCoffe.views import descriptionCoffeCreateListView, descriptionRetrieveUpdateDestroyView
from companyCoffe.views import companyCoffeCreateListView, companyCoffeRetrieveUpdateDestroyView

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('typecoffe/', typeCoffeCreateListView.as_view(), name='typecoffe-list-create'),
    path('typecoffe/<int:pk>/', typeCoffeRetrieveUpdateDestroyView.as_view(), name='typecoffe-detail'),

    path('descriptioncoffe/', descriptionCoffeCreateListView.as_view(), name='descriptioncoffe-list-create'),
    path('descriptioncoffe/<int:pk>/', descriptionRetrieveUpdateDestroyView.as_view(), name='descriptioncoffe-detail'),

    path('companycoffe/', companyCoffeCreateListView.as_view(), name='companycoffe-list-create'),
    path('companycoffe/<int:pk>/', companyCoffeRetrieveUpdateDestroyView.as_view(), name='companycoffe-detail'),
]
