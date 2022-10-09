from Database import *
from Servers import *
import time

if __name__ == "__main__":
    # ##실제 운용 서버 용 인스턴스 생성
    # server_1 = Servers("o1sdp02", "sdp", "10.14.60.2","root","cua001","10.14.119.6","Administrator","48805321",22)
    # server_2 = Servers("o1fdp02", "fdp", "10.14.61.2","root","cua001","10.14.119.8","Administrator","LT7BWPQX",22)
    # #DB로부터 정보 받아와 서버 별 인스턴스 생성
    #

    index = 0
    database = Database()

    while True:
        print("start process")
        for serverInfo in database.readServerInfo():
            print(f"start for server {serverInfo[0]}")
            # 서버 인스턴스 생성
            server = Servers(serverInfo)
            # 서버 및 ilo에서 DATA 받아와 DB 저장
            connect_test_result = server.connection_test()
            server.save_connection_to_db(connect_test_result)
            print(connect_test_result)
            if connect_test_result[0]: #server 연결시
                print(server.get_cmh_info())
                server.save_cmh_to_db(server.get_cmh_info())
                print(server.get_network_info())
                server.save_network_to_db(server.get_network_info())
            if connect_test_result[1]: #ilo 연결시
                print(server.get_ilo_info())
                server.save_ilo_to_db(server.get_ilo_info())
            else : print("Fail to Connect")
        index += 1
        # 대기 - 60초
        time.sleep(60)

