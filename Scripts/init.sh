#!/bin/bash

mkdir -p /home/pi/Documents/PGR_dashboard/log
sudo setfacl -m u:pi:rwx log

sudo apt install -y rclone
sudo pip install -r requirements.txt

sudo echo '
@sh /home/pi/Documents/PGR_dashboard/Scripts/start.sh' >> /etc/xdg/lxsession/LXDE-pi/autostart
sudo echo '
network={
	ssid="PGR Dashboard"
	psk="21rAcing"
	key_mgmt="WPA-PSK"
}' >> /etc/wpa_supplicant/wpa_supplicant.conf

(echo "raspberry"; echo "pgracing"; echo "pgracing") | passwd

(echo "n"; echo "GDrive"; echo "12"; echo ""; echo ""; echo "1"; echo ""; echo ""; echo "y"; echo "n"; echo "y"; )| rclone config

sudo reboot
#pi@raspberrypi:~ $ rclone copy Documents/PGR_dashboard/log/ "GDrive:PGRacing/Logi/"
