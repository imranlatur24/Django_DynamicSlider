from django.shortcuts import render
from .models import SliderModel
# Create your views here.
def index(request):
    carousel = SliderModel.objects.all()
    context  = {
        'carousel' : carousel
    }
    return render(request, "slider.html", context)