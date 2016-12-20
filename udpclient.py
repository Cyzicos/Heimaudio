#!/usr/bin/python

import socket
import sys

UDP_IP = "192.168.178.27" #Zielip
UDP_PORT = 1195
data=sys.argv[1]
MESSAGE = str(data) #Befehl

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))