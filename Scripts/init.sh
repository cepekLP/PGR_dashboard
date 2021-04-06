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
echo "Password changed to pgracing"

rclone_config(){
  rclone config
  echo "Now add at the end of file:"
  echo "*/30 * * * * rclone copy Documents/PGR_dashboard/log/ \"<drive_name>:<path>\""
  echo "Press key to continue"
  read t
}

while true; do
    read -p "Do you wish to congigure rclone?" yn
    case $yn in
        [Yy]* ) rclone_config; break;;
        [Nn]* ) break;;
        * ) echo "Please answer yes or no.";;
    esac
done

echo "Go to Preferences>Raspberry Pi Configuration>Display"
echo "Change Screen blanking from enable to disable"
echo "Press key to continue"
read t
sudo reboot
#pi@raspberrypi:~ $ rclone copy Documents/PGR_dashboard/log/ "GDrive:PGRacing/Logi/"
