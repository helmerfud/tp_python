#! /usr/bin/env python
# -*-coding:UTF-8 -*-
# Exo 12 (c) 2019

#debugage
#import pdb; pdb.set_trace()

import hashlib
from getpass import getpass
chaine_mot_de_passe = "azerty"

mot_de_passe_chiffre = hashlib.sha1(chaine_mot_de_passe).hexdigest()
#mot_de_passe_chiffre = "9cf95dacd226dcf43da376cdb6cbba7035218921"
verrouille = True
while verrouille:
  entre = getpass("Tapez le mot de passe:")
  entre = entre.encode()
  entre_chiffre = hashlib.sha1(entre).hexdigest()
  #print (entre, " - sha1=",entre_chiffre)
  if entre_chiffre == mot_de_passe_chiffre:
    verrouille = False
  else:
    print("Mot de passe incorrecte")
print("Mot de passe accepté...")

