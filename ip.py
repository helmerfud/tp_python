#! /usr/bin/env python 
# -*- coding: UTF-8 -*-
#(c) Xavier 2019

# pour débugger… en ligne de commande !-) 
#import pdb; pdb.set_trace()  

#import socket
import urllib
page = urllib.urlopen("http://www.monip.org/").read() 
ip = page.split("IP : ")[1].split("<br>")[0]
ip1 = page.split("<i>")[1].split("</i>")[0]
print(ip)
print(ip1)

