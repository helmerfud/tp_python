#! /usr/bin/env python
# -*-coding:UTF-8 -*-
# Exo 12 (c) 2019

## Import des librairies
import random
from donnees import *
from fonctions import *

#debugage
#import pdb; pdb.set_trace()

## Declarations
def main():
    correct = 'x000000000000x!!'
    try:
        pscores = loadScore(fileScores)
        print(pscores)
        while correct.lower() != 'o':
            actual_player = raw_input ("Entrer le nom du joueur: ")
            actual_player = str(actual_player)
            print(actual_player, pscores)
            actual_player_score = getScore(actual_player, pscores)

            print(getScore(actual_player, pscores))
            print('actual_player_score: {}'.format(actual_player_score))
            if actual_player_score:
                print ('Joueur, {}, trouvé\n'.format(actual_player))
            else:
                print ('Joueur, {}, non trouvé\n'.format(actual_player))

            correct = raw_input("Continuer ? (O)ui / (N)on: ")
            correct = str(correct)


        #if not actual_player_score:
        #    createPlayer('riri', pscores)
        #    saveScore(pscores, fileScores)
        #
        #idx = random.randint(0,len(fileScores))
        #selected_word = fileScores[idx]

    except KeyboardInterrupt:
        print "Ctrl-C demandé"
    except Exception:
        print "Ici les exceptions"

    exit(0)

if __name__ == "__main__":
    main()
