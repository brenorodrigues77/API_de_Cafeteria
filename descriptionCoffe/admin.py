from django.contrib import admin
from descriptionCoffe.models import descriptionCoffe

@admin.register(descriptionCoffe)
class descriptionCoffeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'creation_date', 'nationality')
