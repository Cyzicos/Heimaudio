# Heimaudio
Auf jedem Slave Pi läuft der udpserver.py. Über diesen server wird der mplayer gesteuert.
Auf dem Master Pi läuft der udpclient.py.

stream starten: "start" senden
ansonsten: mplayer slave befehle senden



Befehl um Server über ssh zu starten:
ssh pi@<IP> python /home/pi/udpServer.py
Befehl in /etc/rc.local einfügen:
/usr/bin/python /home/pi/udpServer.py
davor: chmod a+x /home/pi/udpServer.py
ps -ef | grep python

TODO:
Mehrmals drücken auf Fernbedienung egal


