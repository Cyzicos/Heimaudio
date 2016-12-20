# Heimaudio
Auf jedem Slave Pi läuft der udpserver.py. Über diesen server wird der mplayer gesteuert.
Auf dem Master Pi läuft der udpclient.py. Wichtig: in /opt/fhem legen
Dieser wird über fhem gesteuert.

stream starten: "start" senden
ansonsten: mplayer slave befehle senden


SERVER:
Fifo datei anlegen: /home/pi/mplayerfifo
Befehl um Server über ssh zu starten:
ssh pi@<IP> python /home/pi/udpServer.py

Befehl in /etc/rc.local einfügen:
/usr/bin/python /home/pi/udpserver.py &
davor: chmod a+x /home/pi/udpserver.py
Test ob es geht: ps -ef | grep python



TODO:
Mehrmals drücken auf Fernbedienung egal


