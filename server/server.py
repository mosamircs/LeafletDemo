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

    planes = ["26.8022", "30.8888",
    			 "25.8022", "35.8888",
    			 "23.8022", "33.8888"]
    c.send(bytes(str(len(planes)), 'utf-8'))
    for plane in planes:
    	c.send(bytes(plane, 'utf-8'))
    c.close()
