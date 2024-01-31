from django.contrib import admin
from .models import Meal,Rating 

class RatingAdmin(admin.ModelAdmin):
    list_display=['id','meal','user','stars']
    list_filter=['user','meal']

class Admin(admin.ModelAdmin):
    list_display=['id','title','description']
    list_filter=['title','description']
    search_fields=['title','description']

admin.site.register(Meal,Admin)
admin.site.register(Rating,RatingAdmin)


# Register your models here.
