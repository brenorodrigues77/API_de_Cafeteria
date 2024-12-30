from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('typecoffe', typecoffe.listView.as_view(), name='type-coffe')
]
