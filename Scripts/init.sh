#!/bin/bash

set_up_autostart(){
  echo '@sh /home/pi/Documents/PGR_dashboard/Scripts/start.sh' >> /etc/xdg/lxsession/LXDE-pi/autostart
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

fast_start(){
  sudo systemctl disable dphys-swapfile.service
  sudo systemctl disable apt-daily.service
  sudo systemctl disable hciuart.service
  sudo systemctl disable raspi-config.service
  sudo systemctl disable avahi-daemon.service
  sudo systemctl disable triggerhappy.service
  sudo systemctl disable systemd-udev-trigger.service
  sudo systemctl disable apt-daily-upgrade.timer

  sudo cp /home/pi/Documents/PGR_dashboard/raspberrypi/config.txt /boot/config.txt
  sudo cp /home/pi/Documents/PGR_dashboard/raspberrypi/cmdline.txt /boot/cmdline.txt

}
main(){
  mkdir -p /home/pi/Documents/PGR_dashboard/log
  setfacl -m u:pi:rwx log

  apt install -y python3-pyqt5 python3-gpiozero rclone
  #pip3 install rpi_ws281x

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
