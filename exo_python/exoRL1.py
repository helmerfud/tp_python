#! /usr/bin/env python
# -*-coding:UTF-8 -*-
# Exo 12 (c) 2019

## Import des librairies
import random
from getpass import getpass

#debugage
#import pdb; pdb.set_trace()

## Declarations
def main():
    try:
        x = random.randint(0,10)
        y = 11
        maxtry = 0

        print ('X ', x)

        while maxtry < 15 and x != y:
          y = getpass("Entrer un chiffre entre 0 et 10 :")
          y = int(y.encode())
          if x < y:
            print ("trop grand")
          elif x > y:
            print ("trop petit")
          maxtry += 1

        if x == y:
          #print "Vous avez trouvez, en %d coup" % (maxtry)
          print "Vous avez trouvez le chiffre x ({0}), en {1} coup".format(x,maxtry)
        else:
          print("Nombre de tentative maximum!")

    except KeyboardInterrupt:
        print "Ctrl-C demandé"
    except Exception:
        print "Ici les exceptions"
    exit(0)

if __name__ == "__main__":
    main()
