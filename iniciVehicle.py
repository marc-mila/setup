# -*- coding: utf-8 -*-

import subprocess
import shlex
import sys
import time
import os

ip = raw_input('Introdueix l\'adreça IP del vehicle: ')
cmd = "ssh {} 'hug -f /etc/agent/codes/api.py'".format('pi@' + ip)
 
subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(5)

print "Vehicle  started!"

#sys.exit(0)


