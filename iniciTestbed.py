# -*- coding: utf-8 -*-

import subprocess
import shlex
import sys
import time
import os

#ip = raw_input('Introdueix l\'adreça IP del Testbed: ')
cmd = "ssh {} 'python /home/pi/start.py {}'".format('pi@10.0.1.88', '10.0.1.88')

os.system(cmd)
#sys.exit(0)


