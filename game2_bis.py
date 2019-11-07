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
MIN = 1
MAX = 10

y = 0
cpt=0

#check = [ 1, 2, 3]
check = '123'
level = 0
choix = 0

#####################
## Gestion du MENU ##
#####################


print "\n###################"
print "# CHOIX DU NIVEAU #"
print "# 1 -> FACILE     #"
print "# 2 -> MOYEN      #"
print "# 3 -> DIFFICIL   #"
print "###################\n"

while level != 1 :
  niveau = input ("FAITE VOTRE CHOIX? \n")
  #Dog check Niveau
#  for chiffre in check:
#    if niveau == chiffre :
#      level = 1
#  if level == 0 :
#    print "Mauvais Choix!\n"
  if int(niveau) in check:
    level = 1
  else:
    print "Mauvais Choix!\n"

if niveau == 3 :
  MAX = 1000
elif niveau == 2:
  MAX = 100
else :
  MAX = 10
print "MAX=",MAX

verif = [MIN, MAX +1]
#sys.exit()
# Affection de x
x = random.randint(MIN, MAX)
print(x)

#Boucle tant que x different de y
while x != y:

  # Saisie de y
  y = input("Taper votre chiffre compris entre {0} et {1}? ".format(MIN,MAX))

  #Dog check y compris entre le bornage ( debut et fin)
  if ( (y < verif[0]) && (y > verif[1])):
    print "Mauvais Choix!\n"
  else :
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
