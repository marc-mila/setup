# -*- coding: utf-8 -*-

import subprocess
import shlex
import sys
import time
import os

ip = raw_input('Introdueix l\'adreça IP del testbed: ')
inst = "ssh {} 'sudo apt-get install git'".format('pi@' + ip) 
cmd = "ssh {} 'git clone https://github.com/marc-mila/testbedCodes.git'".format('pi@' + ip)
cmd1 = "ssh {} '/home/pi/testbedCodes/setup.sh {}'".format('pi@' + ip, ip)
cmd2 = "ssh {} 'python /home/pi/testbedCodes/start.py {}'".format('pi@' + ip, ip)

FNULL = open(os.devnull, 'w')
 
subprocess.Popen(shlex.split(inst), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)
subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)
subprocess.Popen(shlex.split(cmd1), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)
subprocess.Popen(shlex.split(cmd2), stdout=FNULL)

print "Testbed started!"

#sys.exit(0)
