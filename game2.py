#! /usr/bin/env python 
# -*- coding: UTF-8 -*-
#(c) Xavier 2019

# pour débugger… en ligne de commande !-) 
#import pdb; pdb.set_trace()

###########################
## Import des LIBRAIRIES ##
###########################
import random

###############################
## Déclaration des Variables ##
###############################
x = random.randint(1, 10)
print(x)
y = 0
cpt=0

#Boucle tant que x different de y
while x != y:
  # Saisie de y
  y = input("Taper votre chiffre compris entre 1 et 10? ")
  # Si trop petit
  if x > y :
    print ("Trop petit\n")
  # Si trop grand
  elif x < y :
    print ("Trop Grand\n")
  cpt += 1

#ancien script
#print ("Gagne c'etait :"+str(x))
#print (" en "+str(cpt)+" coup(s)\n")
# Aff gagné en Xcoups
print ("Gagne c'etait : {0} \n en {1} coup(s)\n".format(x,cpt))

