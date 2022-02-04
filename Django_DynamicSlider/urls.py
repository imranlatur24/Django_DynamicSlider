
from django.contrib import admin
from django.urls import path,include
#loadin images by below pkg
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('slider.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
