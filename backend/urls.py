from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', include('bakery.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('vhod/', views.vhod, name='vhod'),
    path('catalog/', views.catalog, name='catalog'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)