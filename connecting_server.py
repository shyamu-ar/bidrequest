# # def run(host='127.0.0.1', port=22, user='root',
# #                   command='/bin/true', bufsize=-1, key_filename='',
# #                   timeout=120, pkey=None):
# import getpass
# from pexpect import pxssh
# from _datetime import date
# from datetime import datetime
# start = datetime.now()
# file_path = "/home/tr-dt-096/Downloads/"
# # file_path = input("Copy & paste your complete file path without file name ")
# # file_name = input("Enter your file name : ")
# file_name = "bidderServer.08-02-19-09h"
# key_path = "/home/tr-dt-096/Downloads/"
# # key_path = input("Copy & paste your complete key path without key name ")
# key_name = "webairbetakey"
# # server_ip = int(input("Enter your server ip: "))
# server_ip = "103.14.99.220"
# try:  # incase connect fails
#     x = pxssh.pxssh()  # Set x as a variable for pxssh
#     x.login("192.168.1.21", "tr-dt-096", "QSN001")
#     print("Successfully Connected")
#     x.sendline(f"scp -P 7559 -i {key_path+key_name} {file_path+file_name} centos@{server_ip}:")
#     x.sendline(f"ssh -i {key_path+key_name} centos@{server_ip} -p 7559")
#     x.prompt()
#     x.sendline("sudo su")
#     x.prompt()
#     x.sendline("cd /home2/golang/bin")
#     x.prompt()
#     x.sendline(f"mv bidderServer /home2/backup/{file_name}{date.today()}")
#     print(date1)
#     x.prompt()
#     x.sendline(f"mv /home/centos/{file_name} ./bidderServer")
#     x.prompt()
#     id = x.sendline("pidof bidderServer")
#     x.prompt()
#     x.sendline(f"kill -9 {id}")
#     x.prompt()
#     x.sendline("./bidderServer &")
# except Exception as e:  # if fails
#     print(e)
# total = datetime.now() - start
# print(total)
#


import vertica_python
conn_info = {'host': '192.168.1.42', 'port': 5543, 'database': 'mydb',
    'user': 'me', 'password': '123',
    'read_timeout': 600, 'unicode_error': 'strict', 'ssl': False}
print conn_info #check that your information is correct
connection = vertica_python.connect(**conn_info)


