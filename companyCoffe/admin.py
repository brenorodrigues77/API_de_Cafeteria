from django.contrib import admin
from companyCoffe.models import companyCoffe

@admin.register(companyCoffe)
class companyCoffeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'typecoffe', 'release_date', 'resume')
