# import time
#
# from Config.config import login_data
# import subprocess
# import datetime
#
# def connection(username, ip, password):
#     try:
#         connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)
#
#         subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,)
#     except:
#         print("Connection Failed...\nCheck your credentials access...")
#
# # connection super user
# #connection(login_data.linux_username, login_data.ip, login_data.password)
#
# # connection test user
# print("ini")
# print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))
# for i in range(40):
#     print("initialize")
#     print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))
#     #connection(login_data.linux_username, login_data.ip, login_data.password)
#     #connection("itmx16", login_data.ip, "sgeg4913")
#     #connection("itmx16", login_data.ip, "sgeg4913")
#     #connection("itmx17", login_data.ip, "java135")
#     #connection("test18", login_data.ip, "123abc")
#     connection(f"test{str(80+i)}", "192.168.1.30", "123abc")
#     #connection(login_data.linux_username, login_data.ip, login_data.password)
#     #time.sleep(2)
#     print("finish instance")
#     print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))
# print("end")
# print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))

import time

from Config.config import login_data
import subprocess
import datetime


def connection(username, ip, password):
    try:
        connect = 'putty.exe -ssh {}@{} -pw {}'.format(username, ip, password)

        con = subprocess.Popen(connect, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               shell=True, )

    except:
        print("Connection Failed...\nCheck your credentials access...")


# connection super user
connection(login_data.username, login_data.ip, login_data.password)

# connection test user
# for i in range(1):
#
#     print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))
#     #connection(login_data.linux_username, login_data.ip, login_data.password)
#     #connection("itmx16", login_data.ip, "sgeg4913")
#     #connection("itmx16", login_data.ip, "sgeg4913")
#     #connection("itmx17", login_data.ip, "java135")
#     #connection("test18", login_data.ip, "123abc")
#     connection("test80", "192.168.1.30", "123abc")
#     #connection(login_data.linux_username, login_data.ip, login_data.password)
#     #time.sleep(2)
# print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M:%S.%f/"))
#
