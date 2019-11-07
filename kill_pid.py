#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
#(c) Xavier 2019

import subprocess
import signal
import os, sys

name =sys.argv[0]
PID = os.getpid()
stuid = subprocess.getoutput("ps u | grep  " + name + "| awk '{ print $2 }' ")
deaid = subprocess.getoutput("pgrep daemon")
print ("###########")
print ("##"+name+"##")
print (stuid)

#os.kill(stuid, signal.SIGKILL)
print ("##########")
print ("##Daemon##")
print (deaid)
print ("##########")
#os.kill(deaid, signal.SIGKILL)

print ("PID={}".format(PID))
