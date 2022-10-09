from tkinter import CASCADE
from django.db import models
# from django.db.models import F, Sum


class ServerType(models.Model):
    serverType = models.CharField(max_length = 200, default="ETC")

    def __str__(self):
        return self.serverType

class Server(models.Model):
    serverName = models.CharField(max_length=200, null=True)
    serverTypeId = models.ForeignKey(ServerType, on_delete=models.CASCADE)
    linuxIp = models.CharField(max_length=200)
    linuxId = models.CharField(max_length=200, default="root")
    linuxPw = models.CharField(max_length=200, default="cua001")
    iloIp = models.CharField(max_length=200)
    iloId = models.CharField(max_length=200, default = "Administrator")
    iloPw = models.CharField(max_length=200)
    sshPort = models.CharField(max_length=200, default = "22")

    def __str__(self):
        return self.serverName

class Cmh(models.Model):
    id = models.AutoField(primary_key=True)
    serverId = models.ForeignKey(Server, on_delete=models.CASCADE)
    cpu = models.IntegerField()
    cpuStatus = models.BooleanField(default=False)
    mem = models.IntegerField()
    memStatus = models.BooleanField(default=False)
    hdd = models.IntegerField()
    hddStatus = models.BooleanField(default=False)
    time = models.DateTimeField(null=True)

    def __str__(self):
        return self.serverId.serverName

class Network(models.Model):
    id = models.AutoField(primary_key=True)
    serverId = models.ForeignKey(Server, on_delete=models.CASCADE)
    rxPps = models.FloatField()
    txPps = models.FloatField()
    time = models.DateTimeField(null = True)

    def __str__(self):
        return self.serverId.serverName

class Ilo(models.Model):
    id = models.AutoField(primary_key=True)
    serverId = models.ForeignKey(Server, on_delete=models.CASCADE)
    fan1=models.IntegerField(null = True)
    fan1Status = models.BooleanField(default = False)
    fan2=models.IntegerField(null = True)
    fan2Status = models.BooleanField(default=False)
    fan3=models.IntegerField(null = True)
    fan3Status = models.BooleanField(default=False)
    fan4=models.IntegerField(null = True)
    fan4Status = models.BooleanField(default=False)
    cpuThermal=models.FloatField(null = True)
    cpuThermalStatus = models.BooleanField(default=False)
    memThermal=models.FloatField(null = True)
    memThermalStatus = models.BooleanField(default = False)
    time = models.DateTimeField(null = True)

    def __str__(self):
        return self.serverId.serverName

class Connection(models.Model):
    id = models.AutoField(primary_key = True)
    serverId = models.ForeignKey(Server, on_delete=models.CASCADE)
    connectToLinux = models.BooleanField()
    connectToIlo = models.BooleanField()
    def __str__(self):
        return self.serverId.serverName
# Create your models here.
