# Heimaudio
Auf jedem Slave Pi läuft der udpserver.py. Über diesen server wird der mplayer gesteuert.
Auf dem Master Pi läuft der udpclient.py.

stream starten: "start" senden
ansonsten: mplayer slave befehle senden


nohup mplayer -input file=/home/pi/mplayerfifo -playlist /home/pi/swr1bw_mp3_m.m3u  >/dev/null &
Befehl um Server zu starten:
ssh pi@<IP> python /home/pi/udpServer.py


sub startRadio(){
#my($systemcall)=("python udpclient.py start");
my($teststring)="geht";
my($systemcall)=("echo ".$teststring." >> /home/pi/perlog.txt");
print Dumper($systemcall);
system($systemcall);
}

sub muteRadio(){
my($systemcall)=("python udpclient.py m");
system($systemcall);
}
sub quitRadio(){
my($systemcall)=("python udpclient.py quit");
system($systemcall);
}
