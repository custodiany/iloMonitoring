from Database import *
from Servers import *

if __name__=="__main__":
    conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='cua001', port=5432)
    c = conn.cursor()
    # Server instance 생성시 필요한 정보 순서대로 sorting
    c.execute("SELECT \
              serverName, serverType, linuxIp, linuxId, linuxPw, iloIp, iloId, iloPw, sshPort, serverTypeId_id, fanMonitoring_server.id \
              FROM fanMonitoring_server, fanMonitoring_serverType WHERE \
              fanMonitoring_server.serverTypeId_id = fanMonitoring_servertype.id")
    result = c.fetchall()
    print(result)