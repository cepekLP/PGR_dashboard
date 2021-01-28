<h2>Installing dashboard on Rpi</h2>

<h5>Updating</h5>

<code>sudo apt-get update</code>  
<code>sudo apt-get upgrade</code>  
<code>sudo reboot</code>

<h5>Cloning repository</h5>

<code>cd Documents/</code>  
<code>git clone https://github.com/cepekLP/PGR_dashboard</code>  
<code>cd PGR_dashboard/Scripts/</code>  
<code>sudo ./init.sh</code>

<h5>Autostart</h5>

<code>sudo nano /etc/xdg/lxsession/LXDE-pi/autostart</code>

Add at the end:  
<code>@sh /home/pi/Documents/PGR_dashboard/Scripts/start.sh</code>
