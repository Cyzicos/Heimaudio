#!/usr/bin/python 

import socket
import subprocess
import os

UDP_IP = #Meine eigene IP
UDP_PORT = #socket
sock = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
def empfange():
          while True:
                data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
                if data=="start":
                   os.system('mplayer -input file=/home/pi/mplayerfifo -playlist swr1bw_mp3_m.m3u </dev/null >/dev/null 2>&1 &')
                else:
                   cmdstring=("echo %s > /home/pi/mplayerfifo" % (data))
                   os.system(cmdstring)
empfange()