#! /usr/bin/env python3 
# -*- coding: UTF-8 -*-
#(c) Xavier 2019

import re


chaine="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
pseudo = "Bertrand@"
for x in range (0, len(pseudo)):
 m = re.search(pseudo[x], chaine)
 print (m)
