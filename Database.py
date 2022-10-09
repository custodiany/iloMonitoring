import sqlite3
import psycopg2
from datetime import datetime

class Database:
    def readServerInfo(self):
        # conn = sqlite3.connect(self.db_name)
        # c = conn.cursor()
        conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='cua001', port=5432)
        c = conn.cursor()
        # Server instance 생성시 필요한 정보 순서대로 sorting
        c.execute('SELECT \
              "serverName", "serverType", "linuxIp", "linuxId", "linuxPw", "iloIp", "iloId", "iloPw", "sshPort", "serverTypeId_id", "fanMonitoring_server".id \
              FROM "fanMonitoring_server", "fanMonitoring_servertype" WHERE \
              "fanMonitoring_server"."serverTypeId_id" = "fanMonitoring_servertype".id')
        result = c.fetchall()
        return result