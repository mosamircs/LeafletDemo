import socket               

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname() 
port = 12345                
s.bind((host, port))        
s.listen(5)                 

import random
import struct


while True :
    c, addr = s.accept()     
    print(addr)
    # floatlist = [26.80222, 30.8888]
    # msg = struct.pack('%sf' % len(floatlist), *floatlist)

    msg = ["26.80222", "30.8888"]
    c.send(bytes(str(len(msg)), 'utf-8'))
    for each in msg:
    	c.send(bytes(each, 'utf-8'))
    c.close()                
