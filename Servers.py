import os
import paramiko
import time
import sqlite3
from datetime import datetime
from ping3 import ping
import psycopg2


class Servers:
    def __init__(self, serverInfo):
        # server_name = None, server_type = None, server_ip = None, server_id = "root", server_pw = "cua001", ilo_ip = None, \
        # ilo_id = "Administrator", ilo_pw = None, sshport = 22
        self.server_name = serverInfo[0]
        self.server_type = serverInfo[1]
        self.server_ip = serverInfo[2]
        self.server_id = serverInfo[3]
        self.server_pw = serverInfo[4]
        self.ilo_ip = serverInfo[5]
        self.ilo_id = serverInfo[6]
        self.ilo_pw = serverInfo[7]
        self.sshport = serverInfo[8]
        self.servertype_id = serverInfo[9]
        self.server_db_id = serverInfo[10]

    def connection_test(self):
        try :
            result = [0,0,0]
            ################# Ubuntu에서 돌릴때는 -c옵션으로 변경하기!
            r = ping(self.ilo_ip)
            q = ping(self.server_ip)
            if r == False:
                result[1] = False
            else :
                result[1] = True
            if q == False:
                result[0] = False
            else :
                result[0] = True
            result[2] = self.server_db_id
            return result
        except :
            pass


    # ilo서버에서 data 불러와 ./json폴더에 json 형식으로 저장
    def get_ilo_info(self):
        try:
            result = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            self.fanThreshold = 50
            self.thermalThreshold = 80
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ilo_ip, self.sshport, self.ilo_id, self.ilo_pw)
            #fan1_value
            stdin, stdout, stderr = ssh.exec_command("show /system1/fan3")
            result[0] = stdout.readlines()[14][17:19] #나오는 값 보고 체크
            #fan2_value
            stdin, stdout, stderr = ssh.exec_command("show /system1/fan4")
            result[2] = stdout.readlines()[14][17:19] #나오는 값 보고 체크
            #fan3_value
            stdin, stdout, stderr = ssh.exec_command("show /system1/fan5")
            result[4] = stdout.readlines()[14][17:19] #나오는 값 보고 체크
            #fan4_value
            stdin, stdout, stderr = ssh.exec_command("show /system1/fan6")
            result[6] = stdout.readlines()[14][17:19] #나오는 값 보고 체크
            #cpu_thermal_value
            stdin, stdout, stderr = ssh.exec_command("show /system1/sensor2")
            result[8] = stdout.readlines()[14][19:21] #나오는 값 보고 체크
            #mem_thermal_value
            stdin, stdout, stderr = ssh.exec_command("show /system1/sensor6")
            result[10] = stdout.readlines()[14][19:21] #나오는 값 보고 체크
            ssh.close()
            #fan1_status
            self.fan1_value = int(result[0])
            if self.fan1_value > self.fanThreshold or self.fan1_value == 0:
                self.fan1_validity = False
            else:
                self.fan1_validity = True
            result[1] = self.fan1_validity
            #fan2_status
            self.fan2_value = int(result[2])
            if self.fan2_value > self.fanThreshold or self.fan2_value == 0:
                self.fan2_validity = False
            else:
                self.fan2_validity = True
            result[3] = self.fan2_validity
            #fan3_status
            self.fan3_value = int(result[4])
            if self.fan3_value > self.fanThreshold or self.fan3_value == 0:
                self.fan3_validity = False
            else:
                self.fan3_validity = True
            result[5] = self.fan3_validity
            #fan4_status
            self.fan4_value = int(result[6])
            if self.fan4_value > self.fanThreshold or self.fan4_value == 0:
                self.fan4_validity = False
            else:
                self.fan4_validity = True
            result[7] = self.fan1_validity
            #cpu_thermal_status
            self.cpu_thermal_value = int(result[8])
            if self.cpu_thermal_value < self.thermalThreshold:
                self.cpu_thermal_validity = True
            else:
                self.cpu_thermal_validity = False
            result[9] = self.cpu_thermal_validity
            # mem_thermal_status
            self.mem_thermal_value = int(result[10])
            if self.mem_thermal_value < self.thermalThreshold:
                self.mem_thermal_validity = True
            else:
                self.mem_thermal_validity = False
            result[11] = self.mem_thermal_validity
            #server_db_id
            result[12] = self.server_db_id
            #time
            result[13] = datetime.now().isoformat()
            return result
        except : pass

    def get_cmh_info(self):
        try :
            self.cmhThreshold = 80
            result = [0,0,0,0,0,0,0,0]
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.server_ip, self.sshport, self.server_id, self.server_pw)
            #cpu
            stdin, stdout, stderr = ssh.exec_command("sar -u | awk '/Average/{print(100-$NF)}'")
            result[0] = stdout.read().strip().decode("utf-8")
            #mem
            stdin, stdout, stderr = ssh.exec_command("sar -r | awk '/Average/{print $4}'")
            result[2] = stdout.read().strip().decode("utf-8")
            #disk
            stdin, stdout, stderr = ssh.exec_command("df -h | awk 'NR>=2 {print $5}'")
            result[4] = max([int(l.strip()[0:-1]) for l in stdout.readlines()])
            ssh.close()
            self.cpu_value = float(result[0])
            self.mem_value = float(result[2])
            self.disk_value = float(result[4])
            #cpu_status
            if self.cpu_value < self.cmhThreshold:
                self.cpu_validity = True
            else:
                self.cpu_validity = False
            result[1] = self.cpu_validity
            #mem_status
            if self.mem_value < self.cmhThreshold:
                self.mem_validity = True
            else:
                self.mem_validity = False
            result[3] = self.mem_validity
            #disk_status
            if self.disk_value < self.cmhThreshold:
                self.disk_validity = True
            else:
                self.disk_validity = False
            result[5] = self.disk_validity
            result[6] = time.time()
            result[7] = self.server_db_id
            return result
        except : pass

    def get_network_info(self):
        try :
            speed = {}
            result = [0,0,0,0]
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.server_ip, self.sshport, self.server_id, self.server_pw)
            stdin, stdout, stderr = ssh.exec_command("netstat -i | awk 'NR==3 {print $4}'")
            speed["before_rx"] = stdout.read().strip().decode("utf-8")
            stdin, stdout, stderr = ssh.exec_command("netstat -i | awk 'NR==3 {print $8}'")
            speed["before_tx"] = stdout.read().strip().decode("utf-8")
            time.sleep(5)
            stdin, stdout, stderr = ssh.exec_command("netstat -i | awk 'NR==3 {print $4}'")
            speed["after_rx"] = stdout.read().strip().decode("utf-8")
            stdin, stdout, stderr = ssh.exec_command("netstat -i | awk 'NR==3 {print $8}'")
            speed["after_tx"] = stdout.read().strip().decode("utf-8")
            #get rxPps
            result[0] = '%0.3f' %((float(speed["after_rx"]) - float(speed["before_rx"]))/5)
            #get txPps
            result[1] = '%0.3f' %((float(speed["after_tx"]) - float(speed["before_tx"]))/5)
            #get time and server_db_id
            result[2] = 0
            result[3] = self.server_db_id
            return result
        except : pass



    def save_cmh_to_db(self, cmhInfoList):
        try:
            self.table_name = "fanMonitoring_cmh"
            self.input_name1, self.input_name2, self.input_name3, self.input_name4, self.input_name5, self.input_name6, self.input_name7, self.input_name8 \
                = ["cpu", "cpuStatus", "mem", "memStatus", "hdd", "hddStatus", "time", "serverId_id"]
            self.input_data1, self.input_data2, self.input_data3, self.input_data4, self.input_data5, self.input_data6, self.input_data7, self.input_data8,\
                = cmhInfoList


            conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='cua001', port=5432)
            c = conn.cursor()
            c.execute(f'INSERT INTO "{self.table_name}" ("{self.input_name1}", "{self.input_name2}", "{self.input_name3}", "{self.input_name4}", "{self.input_name5}",\
                                              "{self.input_name6}", "{self.input_name7}", "{self.input_name8}") VALUES ({self.input_data1},{self.input_data2}, {self.input_data3}, {self.input_data4}, {self.input_data5}, {self.input_data6}, current_timestamp, {self.input_data8})')
            conn.commit()
            conn.close()
        except:pass



    def save_network_to_db(self, networkInfoList):
        try:
            self.table_name = "fanMonitoring_network"
            self.input_name1, self.input_name2, self.input_name3, self.input_name4 = ["rxPps", "txPps", "time", "serverId_id"]
            self.input_data1, self.input_data2, self.input_data3, self.input_data4 = networkInfoList
            conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='cua001', port=5432)
            c = conn.cursor()
            c.execute(f'INSERT INTO "{self.table_name}" ("{self.input_name1}", "{self.input_name2}", "{self.input_name3}", "{self.input_name4}") VALUES \
                      ({self.input_data1}, {self.input_data2}, current_timestamp, {self.input_data4})')
            conn.commit()
            conn.close()
        except : pass


    def save_ilo_to_db(self, iloInfoList):
        try:
            self.table_name = "fanMonitoring_ilo"
            self.input_name1 = "fan1"
            self.input_name2 = "fan1Status"
            self.input_name3 = "fan2"
            self.input_name4 = "fan2Status"
            self.input_name5 = "fan3"
            self.input_name6 = "fan3Status"
            self.input_name7 = "fan4"
            self.input_name8 = "fan4Status"
            self.input_name9 = "cpuThermal"
            self.input_name10 = "cpuThermalStatus"
            self.input_name11 = "memThermal"
            self.input_name12 = "memThermalStatus"
            self.input_name13 = "serverId_id"
            self.input_name14 = "time"
            self.input_data1, self.input_data2, self.input_data3, self.input_data4, self.input_data5, self.input_data6, \
            self.input_data7,self.input_data8, self.input_data9, self.input_data10, self.input_data11, self.input_data12, \
            self.input_data13, self.input_data14 = iloInfoList

            conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='cua001', port=5432)
            c = conn.cursor()
            c.execute(f'INSERT INTO "{self.table_name}" ("{self.input_name1}", "{self.input_name2}", "{self.input_name3}", "{self.input_name4}", \
            "{self.input_name5}", "{self.input_name6}", "{self.input_name7}", "{self.input_name8}", "{self.input_name9}", "{self.input_name10}", \
            "{self.input_name11}", "{self.input_name12}", "{self.input_name13}", "{self.input_name14}") VALUES ({self.input_data1}, {self.input_data2}, {self.input_data3}, {self.input_data4}, {self.input_data5}, {self.input_data6}, {self.input_data7}, \
             {self.input_data8},{self.input_data9}, {self.input_data10}, {self.input_data11}, {self.input_data12}, {self.input_data13}, current_timestamp)'\
            )
            conn.commit()
            conn.close()
        except: pass


    def save_connection_to_db(self, connectionInfoList):
        try:
            self.table_name = "fanMonitoring_connection"
            self.input_name1 = "connectToLinux"
            self.input_name2 = "connectToIlo"
            self.input_name3 = "serverId_id"
            self.input_data1 = connectionInfoList[0]
            self.input_data2 = connectionInfoList[1]
            self.input_data3 = connectionInfoList[2]

            conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='cua001', port=5432)
            c = conn.cursor()
            c.execute(f'INSERT INTO "{self.table_name}" ("{self.input_name1}", "{self.input_name2}", "{self.input_name3}") VALUES ({self.input_data1}, {self.input_data2}, {self.input_data3})')
            conn.commit()
            conn.close()
        except : pass