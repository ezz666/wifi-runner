#!/usr/bin/env python
def ParseConfig(config_name):
    import ConfigParser
    cf = ConfigParser.ConfigParser()
    cf.read(config_name)
    result_dict = {}
    for sec in cf.sections():
        result_dict[sec] = {}
        for opt in cf.options(sec):
            result_dict[sec][opt] = cf.get(sec,opt)
        if not result_dict[sec]:
            del result_dict[sec]
    return result_dict
    
def GetServiceName():
    global manager
    services = manager.GetServices()
    # we are looking only for wifi connections
    online_service = filter(lambda x: x[1]["Type"]==dbus.String(u"wifi"), services)
    # State is 'ready' means that ip was set.
    online_service = filter(lambda x: x[1]["State"]in (dbus.String(u"online"),dbus.String(u'ready')),online_service)
    if online_service:
        if "Name" in online_service[0][1]:		
            return online_service[0][1]["Name"]
    return None

def script_run(name,action):
    global conf,path
    if name in conf:
        if action in conf[name]:
            script = conf[name][action]
            if script[0]!='/':
                script = os.path.join(path,script)
            try:
                subprocess.Popen(script.split(),stdout=sys.stdout,stderr=sys.stderr)
            except OSError:
                print "Something went wrong with script", script

def hand_func(pname, value):
    global name, default
    if value == 1:
        name = GetServiceName()
        action = "start"
    else: action ="stop"
    script_run(name,action)
    script_run(default,action)
    if (value==0): name = None

conf_name="/home/nemo/.config/systemd/scripts/wifi-runner.conf"
conf = ParseConfig(conf_name)
default = "                 Default                  "
import os.path
path = os.path.dirname(os.path.abspath(conf_name))

import dbus,subprocess,sys
import gi.overrides.GObject as gobject
from dbus.mainloop.glib import DBusGMainLoop
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()
bus.add_signal_receiver(hand_func,signal_name="PropertyChanged",dbus_interface="net.connman.Technology",path="/net/connman/technology/wifi",arg0="Connected")
manager = dbus.Interface(bus.get_object("net.connman", "/"), "net.connman.Manager")
name = GetServiceName()
loop=gobject.MainLoop()
loop.run()

