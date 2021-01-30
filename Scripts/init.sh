#!/bin/bash
mkdir -p /home/pi/Documents/PGR_dashboard/log
sudo setfacl -m u:pi:rwx log
sudo apt-get install python3-pyqt5
sudo apt install python3-gpiozero
sudo echo '
@sh /home/pi/Documents/PGR_dashboard/Scripts/start.sh' >> /etc/xdg/lxsession/LXDE-pi/autostart
sudo reboot
