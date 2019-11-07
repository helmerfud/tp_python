#! /usr/bin/env python 
# -*- coding: UTF-8 -*-
#(c) Xavier 2019

# pour débugger… en ligne de commande !-) 
#import pdb; pdb.set_trace()

x = 1
y = 1
while x != y:
  if x > y:
    print ("x est supérieur à y")
  if x < y:
    print ("x est inférieur à y")

if x == y:
  print ("x est égale à y")

