from Database import *
from Servers import *
from ping3 import ping
import psycopg2

if __name__=="__main__":
    # conn = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='cua001', port=5432)
    # c = conn.cursor()
    # c.execute('SELECT COUNT(*) FROM "fanMonitoring_servertype"')
    # result = c.fetchone()
    # print(type(result[0]))
    for i in range(1,13):
        print(i)