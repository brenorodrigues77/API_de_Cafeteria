from django.contrib import admin
from django.urls import path
from typeCoffe.views import typeCoffeCreateListView, typeCoffeRetrieveUpdateDestroyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('typecoffe/', typeCoffeCreateListView.as_view(), name='typecoffe-list-create'),
    path('typecoffe/<int:pk>/',typeCoffeRetrieveUpdateDestroyView.as_view(),name='typecoffe-detail')
]
