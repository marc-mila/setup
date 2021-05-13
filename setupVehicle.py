# -*- coding: utf-8 -*-

import subprocess
import shlex
import sys
import time
import os

ip = raw_input('Introdueix l\'adreça IP del vehicle: ')
cmd = "ssh {} 'git clone https://github.com/marc-mila/setupVehicle.git'".format('pi@' + ip)
cmd1 = "ssh {} '/home/pi/setupVehicle/setup.sh'".format('pi@' + ip)
cmd2 = "ssh {} 'sudo rm -r /home/pi/setupVehicle'".format('pi@' + ip)
cmd3 = "ssh {} 'sudo rm -r /home/pi/codesVehicles'".format('pi@' + ip)
FNULL = open(os.devnull, 'w')
 
subprocess.Popen(shlex.split(cmd2), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)
subprocess.Popen(shlex.split(cmd3), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)
subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)
subprocess.Popen(shlex.split(cmd1), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)

print "Vehicle  started!"

#sys.exit(0)
