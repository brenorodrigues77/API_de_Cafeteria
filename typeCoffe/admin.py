from django.contrib import admin
from typeCoffe.models import typeCoffe

@admin.register(typeCoffe)
class typeCoffeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')