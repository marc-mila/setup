# -*- coding: utf-8 -*-

import subprocess
import shlex
import sys
import time
import os

ip = raw_input('Introdueix l\'adreça IP del Testbed: ')
cmd = "ssh {} 'python /home/pi/start.py {}'".format('pi@' + ip, ip)
 
subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)

print "Testbed started!"

#sys.exit(0)


