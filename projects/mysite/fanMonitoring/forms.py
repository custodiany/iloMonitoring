# from django import forms
# from fanMonitoring.models import *
# # from datetimewidget.widgets import DateTimeWidget
#
#
#
#
#
#
# class ServerForm(forms.ModelForm):
#     class Meta :
#         model = Server
#         fields = ['serverName', 'serverTypeId', 'linuxIp', 'linuxId', 'linuxPw', 'iloIp', 'iloId', 'iloPw', 'sshPort']
#
#         labels = {
#             'serverName' : '서버 이름',
#             'serverTypeId' : '서버 종류',
#             'linuxIp' : '서버 IP',
#             'linuxId' : '서버 ID',
#             'linuxPw' : '서버 PW',
#             'iloIp' : 'ILO IP',
#             'iloId' : 'ILO ID',
#             'iloPw' : 'ILO PW',
#             'sshPort' : 'SSH PORT',
#         }
#
#
# class ServerTypeForm(forms.ModelForm):
#     class Meta :
#         model = ServerType
#         fields = ['serverType']
#
#         labels = {
#             'serverType' : '서버 종류',
#         }