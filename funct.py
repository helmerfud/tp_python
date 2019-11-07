#! /usr/bin/env python 
# -*- coding: UTF-8 -*-
#(c) Xavier 2019

# pour débugger… en ligne de commande !-) 
#import pdb; pdb.set_trace()

###########################
## Import des LIBRAIRIES ##
###########################
import time
import os
import sys

#Cls
os.system('cls' if os.name == 'nt' else 'clear')

##############
## Function ##
##############

###########################
## Function tradj()      ##
## Entrée 0              ##
## Sortie jours en texte ##
###########################
def tradj():
  jour_en =  time.strftime('%A') 
  j_en = ['Monday','Tuesday']
  j_fr = ['Lundi','Mardi']
  for x in range (0,2) :
    #print x
    if jour_en == j_en[x] :
      jour =  j_fr[x]
  return str(jour)

##########################
## Function tradm()     ##
## Entrée 0             ##
## Sortie mois en texte ##
##########################
def tradm():
  mois_en =  time.strftime('%B') 
  m_en = ['Junary','April']
  m_fr = ['Janvier','Avril']
  for x in range (0,2) :
    #print x
    if mois_en == m_en[x] :
      mois =  m_fr[x]
  return str(mois)

###############################
## Déclaration des Variables ##
###############################


###############
## Principal ##
###############
if __name__ == '__main__':
  #print traduction()
  #sys.exit()
  jour_fr =tradj()
  mois_fr =tradm()
  print time.strftime('%A %d %B %Y %H:%M:%S')
  print  str(jour_fr) + time.strftime(' %d ') + str(mois_fr) + time.strftime(' %Y %H:%M:%S')

