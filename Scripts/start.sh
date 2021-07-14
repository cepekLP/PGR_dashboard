#!/bin/bash
cd /home/pi/Documents/PGR_dashboard
if [[ -f /log/Points.json ]]; then
  cp /log/Points.json /Points.json
fi

sudo python3 run.py &
sudo python3 Workers/ gcd.py &
sleep 0.2
exec /sbin/init
