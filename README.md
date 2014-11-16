wifi-runner
===========

Run scripts when wifi connection (guided by connman) state is changed. 

The Connman connection manager on Sailfish unfortunately doesn't provide the ability
to run scripts after the wifi connection was established.

The purpose of this project is in adding this feature.
Here we have simple daemon that listening to connman's dbus interface.

Install
===========
copy the systemd folder contents ~/.config/systemd
and enable the service:
$ systemctl --user enable wifi-runner.service

After reboot this daemon will start automatically.

Configure
===========
There is a config file systemd/scripts/wifi-runner.conf .
It's name and path are hardcoded in wifi-runner.py so
after installation it's worth to check it is correct.

Each section name corresponds to SSID of the network.
Default section corresponds to scripts that runned for all wifi networks.
It's name consists of 42 charactes so it won't correspond to any correct SSID (the limit is 32).

For example if we want to start script ./test.py
when wifi with SSID 'TEST' stops and start.sh when it starts
we can just add in the end of the file

[TEST]

start = start.sh

stop  = test.py


Paths to scripts can be relative to config file or an absolute one.

Script and configuration that auto authorize you in Moscow Metro Free Wifi are included.
