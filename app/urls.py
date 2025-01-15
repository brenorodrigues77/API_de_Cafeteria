from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path('api/v1/', include('typeCoffe.urls')),
    path('api/v1/', include('companyCoffe.urls')),
    path('api/v1/', include('descriptionCoffe.urls')),
    path('api/v1/', include('reviewCoffe.urls')),
]
