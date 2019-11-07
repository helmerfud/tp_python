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
    temp_word = "111111111111111"
    nb_try = 0
    try:
        pscores = loadScore(fileScores)
        while correct.lower() != 'o':
            actual_player = myInput ("Entrer le nom du joueur: ", '^[a-zA-Z]{1,10}$')
            if not actual_player:
                continue
            actual_player = str(actual_player)
            actual_player_score = getScore(actual_player, pscores)

            print('actual_player_score: {}\n'.format(actual_player_score))
            if actual_player_score:
                print ('Joueur, {}, trouvé. Votre score est de: {}'.format(actual_player, actual_player_score))
            else:
                print ('Joueur, {}, non trouvé\n'.format(actual_player))

            correct = myInput("Continuer ? (O)ui / (N)on: ", '^[a-zA-Z]$')

        if not actual_player_score:
            createPlayer(actual_player, pscores)
            saveScore(pscores, fileScores)

        idx = random.randint(0,len(liste_mots)-1)
        selected_word = liste_mots[idx]
        print("Le mot a trouver contient {} lettres\n\n".format(len(selected_word)))
        print("Nombre de tentaives maximum: {}".format(max_try))

        temp_word = "_".center(len(selected_word), '_')
        print('--> {}'.format(temp_word))

        while temp_word != selected_word and nb_try < max_try:
            letter = myInput("Entrer un lettre: ", '^[a-zA-Z]$')
            print('lettre {}'.format(letter))
            if letter in selected_word:
                #print('trouve: {}.'.format(letter))
                for key, val in enumerate(selected_word):
                    if val == letter:
                        temp_word = repl_char(temp_word, val, key)
                print('-->: {}'.format(temp_word))
                nb_try += 1
                print("Nombre de tentaives restante: {}".format(max_try - nb_try))
            else:
                nb_try += 1
                print('--> {}'.format(temp_word))
                print("Nombre de tentaives restante: {}".format(max_try - nb_try))

        if (nb_try >= max_try and temp_word != selected_word):
            print("Nombre de tentatives épuisées\n")
        else:
            print("Vous avez trouvé\n")
            print("Votre score est de {} points".format(max_try - nb_try))
            setScore(actual_player, actual_player_score + (max_try - nb_try), pscores)
            saveScore(pscores, fileScores)
    except KeyboardInterrupt:
        print "Ctrl-C demandé"
    except Exception:
        print "Ici les exceptions"

    exit(0)

if __name__ == "__main__":
    main()
