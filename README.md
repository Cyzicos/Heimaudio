# Heimaudio
Auf jedem Pi läuft der udpserver.py. Über diesen server wird der mplayer gesteuert.

stream starten: "start" senden
ansonsten: mplayer slave befehle senden


nohup mplayer -input file=/home/pi/mplayerfifo -playlist /home/pi/swr1bw_mp3_m.m3u  >/dev/null &
