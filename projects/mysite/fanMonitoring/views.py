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
    pass

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

