from sys import flags
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
# from numpy import _FlatIterSelf
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import F, Sum
from django.db import models
import datetime

# Create your views here.


def index(request):
    servers = Server.objects.all()
    connections = Connection.objects.all().order_by('-id')
    context = {'servers':servers, 'connections' : connections}
    return render(request, 'fanMonitoring/index.html', context)

def registrationServerType(request):
    pass

def registrationServer(request):
    pass

def cmh(request):
    serverType = request.GET.get('serverType', '1')
    rtime = Cmh.objects.filter(serverId__serverTypeId=serverType).values('time').latest('id')
    servers = Cmh.objects.filter(serverId__serverTypeId = serverType).values('serverId__serverName', 'cpu', 'cpuStatus', 'mem', 'memStatus', 'hdd', 'hddStatus').distinct()
    context = {'servers' : servers, 'serverType' : serverType, 'rtime' : rtime}
    return render(request, 'fanMonitoring/cmh.html', context)

def network(request):
    serverType = request.GET.get('serverType', '1')
    servers = Network.objects.filter(serverId__serverTypeId=serverType).values('serverId__serverName', 'rxPps', 'txPps', 'time'
                                                                               ).order_by('-id')
    context = {'servers': servers, 'serverType': serverType}
    return render(request, 'fanMonitoring/network.html', context)

def iloInfo(request):
    serverType = request.GET.get('serverType', '1')
    rtime = Ilo.objects.filter(serverId__serverTypeId=serverType).values('time').latest('id')
    servers = Ilo.objects.filter(serverId__serverTypeId=serverType).values('serverId__serverName', 'fan1', 'fan1Status','fan2', 'fan2Status', \
                                                                           'fan3', 'fan3Status','fan4', 'fan4Status', 'cpuThermal', 'cpuThermalStatus',\
                                                                            'memThermal', 'memThermalStatus').distinct()
    context = {'servers': servers, 'serverType': serverType, 'rtime': rtime}
    return render(request, 'fanMonitoring/ilo.html', context)

def logHome(request):
    pass

def logCmh(request):
    pass

def logNetwork(request):
    pass

def logIloInfo(request):
    pass

