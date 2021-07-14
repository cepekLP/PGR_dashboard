#!/bin/bash
cd /home/pi/Documents/PGR_dashboard
if [[ -f /log/Points.json ]]; then
  cp /log/Points.json /Points.json
fi

sudo python3 run.py &
sleep 0.2
sudo python3 Workers/gcd.py &
exec /sbin/init
