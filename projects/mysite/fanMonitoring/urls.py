from django.urls import path, include
from . import views

app_name = 'fanMonitoring'

urlpatterns = [
    path('', views.index, name='index'),
    path('cmh/', views.cmh, name='cmh'),
    path('network/', views.network, name='network'),
    path('iloInfo/', views.iloInfo, name='iloInfo'),
    path('logHome', views.logHome, name='logHome'),
    path('logCmh', views.logCmh, name='logCmh'),
    path('logNetwork', views.logNetwork, name='logNetwork'),
    path('logIloInfo', views.logIloInfo, name='logIloInfo'),
    path('registrationServerType', views.registrationServerType, name='registrationServerType'),
    path('registrationServer', views.registrationServer, name='registrationServer'),
]