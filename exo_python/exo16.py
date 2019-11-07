#! /usr/bin/env python
# -*-coding:UTF-8 -*-
# Exo 13 (c) 2019


date = "Lundi 8 avril 2019"
print len(date)
print date[0:1]

for lettre in date:
  if lettre == "i":
     lettre = "o"
  print (lettre)
