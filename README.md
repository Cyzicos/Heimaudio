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
Test ob Python Programm läuft: ps -ef | grep python
pidof "Programmname" #Findet Prozess eines programmes

Shairplay-sync: shairport-sync -a "TestAirplay"


Mplayer Fixing hifiberry: https://support.hifiberry.com/hc/en-us/community/posts/201841301-No-sound-out-of-hifiberry

TODO:
Mehrmals drücken auf Fernbedienung egal


