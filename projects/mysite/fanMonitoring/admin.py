from django.contrib import admin
from .models import *


# Register your models here.

class CmhAdmin(admin.ModelAdmin):
    list_display=['time', 'serverId', 'cpu', 'mem', 'hdd' ]
    list_filter = ['serverId']

class IloAdmin(admin.ModelAdmin):
    list_display=['time', 'serverId', 'fan1', 'fan2', 'fan3', 'fan4', 'cpuThermal', 'memThermal' ]
    list_filter = ['serverId']

class NetworkAdmin(admin.ModelAdmin):
    list_display=['time', 'serverId', 'rxPps', 'txPps' ]
    list_filter = ['serverId']

admin.site.register(Server)
admin.site.register(ServerType)
admin.site.register(Cmh, CmhAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Ilo, IloAdmin)