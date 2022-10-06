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
    context = {'servers':servers}
    return render(request, 'fanMonitoring/index.html', context)

def registrationServerType(request):
    pass

def registrationServer(request):
    pass

def cmh(request):
    serverType = request.GET.get('serverType', '')
    sdps = Cmh.objects.filter(serverId__serverTypeId = 1).last() #최근값만 가져옴.
    fdps = Cmh.objects.filter(serverId__serverTypeId = 2).last()
    drfs = Cmh.objects.filter(serverId__serverTypeId = 3).values().last()
    sdrs = Cmh.objects.filter(serverId__serverTypeId = 4).values().last()
    efss = Cmh.objects.filter(serverId__serverTypeId = 5).values().last()
    rcoms = Cmh.objects.filter(serverId__serverTypeId = 6).values().last()
    byps = Cmh.objects.filter(serverId__serverTypeId = 7).values().last()
    tsvs = Cmh.objects.filter(serverId__serverTypeId = 8).values().last()
    apps = Cmh.objects.filter(serverId__serverTypeId = 9).values().last()
    nmss = Cmh.objects.filter(serverId__serverTypeId = 10).values().last()
    pmss = Cmh.objects.filter(serverId__serverTypeId = 11).values().last()
    wass = Cmh.objects.filter(serverId__serverTypeId = 12).values().last()
    etcs = Cmh.objects.filter(serverId__serverTypeId = 13).values().last()
    context = {'sdps' : sdps, 'fdps' : fdps, 'drfs' : drfs, 'sdrs' : sdrs, 'efss' : efss, 'rcoms' : rcoms, 'byps' : byps,\
               'tsvs' : tsvs, 'apps' : apps, 'nmss' : nmss, 'pmss' : pmss, 'wass' : wass, 'etcs' : etcs}
    return render(request, 'fanMonitoring/cmh.html', context)

def network(request):
    pass

def iloInfo(request):
    pass

def logHome(request):
    pass

def logCmh(request):
    pass

def logNetwork(request):
    pass

def logIloInfo(request):
    pass

