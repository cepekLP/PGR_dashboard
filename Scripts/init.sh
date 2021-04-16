#!/bin/bash

set_up_autostart(){
  echo '[Unit]
Description=My service
After=network.target

[Service]
ExecStart=/usr/bin/python3 -u main.py
WorkingDirectory=/home/pi/myscript
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=graphical.target' > /etc/systemd/system/dashboard.service
  systemctl enable dashboard.service
}

set_up_wifi(){
echo '
network={
	ssid="PGR Dashboard"
	psk="21rAcing"
	key_mgmt=WPA-PSK
}' >> /etc/wpa_supplicant/wpa_supplicant.conf
}

change_password(){
  (echo "raspberry"; echo "pgracing"; echo "pgracing") | passwd
  echo "Password changed to \"pgracing\""

}

rclone_config(){
  rclone config
  LIST=$(rclone listremotes)
  echo "*/30 * * * * rclone copy Documents/PGR_dashboard/log/ {$LIST}PGRacing/log" >> etc/crontab
}
main(){
  mkdir -p /home/pi/Documents/PGR_dashboard/log
  setfacl -m u:pi:rwx log

  apt install -y python3-pyqt5 python3-gpiozero rclone

  set_up_autostart
  set_up_wifi
  change_password

  while true; do
      read -p "Do you wish to congigure rclone [y/n]?" yn
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
  reboot
}

main
