from django.contrib import admin
from django.urls import path, include
from django.conf.urls import(handler404, handler500)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fanMonitoring.urls')),
    #path('common/', include('common.urls')),
]
