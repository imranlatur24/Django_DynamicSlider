from django.contrib import admin
from .models import SliderModel
# Register your models here.

@admin.register(SliderModel)
class SliderAdmin(admin.ModelAdmin):
    list_display=['id','image','title','sub_title']

