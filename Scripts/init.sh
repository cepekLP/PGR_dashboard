#!/bin/bash

mkdir -p /home/pi/Documents/PGR_dashboard/log
sudo setfacl -m u:pi:rwx log

sudo apt install -y python3-pyqt5 python3-gpiozero rclone

sudo echo '
@sh /home/pi/Documents/PGR_dashboard/Scripts/start.sh' >> /etc/xdg/lxsession/LXDE-pi/autostart
sudo echo '
network={
	ssid="PGR Dashboard"
	psk="21rAcing"
	key_mgmt="WPA-PSK"
}' >> /etc/wpa_supplicant/wpa_supplicant.conf

echo -e "raspberry\npgracing\npgracing" | passwd

echo -e "n\nGDrive\n12\n\n\n1\n\n\ny\nn\ny" | rclone config

sudo reboot
#pi@raspberrypi:~ $ rclone copy Documents/PGR_dashboard/log/ "GDrive:PGRacing/Logi/"
