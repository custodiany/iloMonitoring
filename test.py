from Database import *
from Servers import *
from ping3 import ping

if __name__=="__main__":
    # speed = {}
    # result = [0, 0, 0, 0]
    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect('10.14.60.2', '22', 'root', 'cua001')
    # stdin, stdout, stderr = ssh.exec_command("netstat -i | awk 'NR==3 {print $4}'")
    # speed["before_rx"] = stdout.read().strip().decode("utf-8")
    # stdin, stdout, stderr = ssh.exec_command("netstat -i | awk 'NR==3 {print $8}'")
    # speed["before_tx"] = stdout.read().strip().decode("utf-8")
    # time.sleep(1)
    # stdin, stdout, stderr = ssh.exec_command("netstat -i | awk 'NR==3 {print $4}'")
    # speed["after_rx"] = stdout.read().strip().decode("utf-8")
    # stdin, stdout, stderr = ssh.exec_command("netstat -i | awk 'NR==3 {print $8}'")
    # speed["after_tx"] = stdout.read().strip().decode("utf-8")
    # # get rxPps
    # result[0] = '%0.3f' % ((float(speed["after_rx"]) - float(speed["before_rx"])))
    # # get txPps
    # result[1] = '%0.3f' % ((float(speed["after_tx"]) - float(speed["before_tx"])))
    # # get time and server_db_id
    # result[2] = 0
    # result[3] = 0
    # print(result)
    print(ping('10.14.60.11'))