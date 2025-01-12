from django.contrib import admin
from reviewCoffe.models import reviewCoffe

@admin.register(reviewCoffe)
class reviewCoffeAdmin(admin.ModelAdmin):
    list_display = ('companycoffe', 'stars', 'comment')
