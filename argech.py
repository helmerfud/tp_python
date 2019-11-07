#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
#(c) Xavier 2019

import sys

for arg in sys.argv:
    print (arg)

HOST = sys.argv[1]
PORT = sys.argv[2]
print ("ADDR: {} {}".format(HOST,PORT))

