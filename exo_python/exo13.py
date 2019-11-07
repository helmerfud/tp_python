#! /usr/bin/env python
# -*-coding:UTF-8 -*-
# Exo 13 (c) 2019

#debugage
#import pdb; pdb.set_trace()
import random
import sys
import time

i = 0
while i < 20:
  sys.stdout.write("1")
  sys.stdout.flush()
  attente = 0.2
  attente += random.randint(1,60) / 100
  time.sleep(attente)
  i += 1
print("\n")
