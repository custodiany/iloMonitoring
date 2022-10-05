import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name = "./projects/mysite/db.sqlite3"):
        self.db_name = db_name

    def readServerInfo(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        # Server instance 생성시 필요한 정보 순서대로 sorting
        c.execute("SELECT \
                  serverName, serverType, linuxIp, linuxId, linuxPw, iloIp, iloId, iloPw, sshPort, serverTypeId_id, fanMonitoring_server.id \
                  FROM fanMonitoring_server, fanMonitoring_serverType WHERE \
                  fanMonitoring_server.serverTypeId_id = fanMonitoring_servertype.id")
        result = c.fetchall()
        return result