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
    connections = Connection.objects.all().order_by('serverId', '-id').distinct('serverId')
    context = {'servers':servers, 'connections' : connections}
    return render(request, 'fanMonitoring/index.html', context)

def registrationServerType(request):
    pass

def registrationServer(request):
    pass

def cmh(request):
    serverType = request.GET.get('serverType', '')
    rtime = Cmh.objects.all().values('time').latest('id')
    servers = Cmh.objects.all().order_by('serverId', '-id').distinct('serverId')
    if serverType:
        try :
            rtime = Cmh.objects.filter(serverId__serverTypeId=serverType).values('time').latest('id')
            servers = Cmh.objects.filter(serverId__serverTypeId=serverType).order_by('serverId', '-id').distinct('serverId')
        except Cmh.DoesNotExist:
            rtime = {'time' : "File does not exist"}
            servers = None
    context = {'servers' : servers, 'serverType' : serverType, 'rtime' : rtime}
    return render(request, 'fanMonitoring/cmh.html', context)

def network(request):
    serverType = request.GET.get('serverType', '')
    servers = Network.objects.all().order_by('serverId', '-id').distinct('serverId')
    if serverType:
        try :
            servers = Network.objects.filter(serverId__serverTypeId=serverType).order_by('serverId', '-id').distinct(
                'serverId')
        except Network.DoesNotExist:
            servers = None
    context = {'servers': servers, 'serverType': serverType}
    return render(request, 'fanMonitoring/network.html', context)

def iloInfo(request):
    serverType = request.GET.get('serverType', '')
    rtime = Ilo.objects.all().values('time').latest('id')
    servers = Ilo.objects.all().order_by('serverId', '-id').distinct('serverId')
    if serverType:
        try :
            rtime = Ilo.objects.filter(serverId__serverTypeId=serverType).values('time').latest('id')
            servers = Ilo.objects.filter(serverId__serverTypeId=serverType).order_by('serverId', '-id').distinct('serverId')
        except Ilo.DoesNotExist :
            rtime = {'time' : "File does not exist"}
            servers = None
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


