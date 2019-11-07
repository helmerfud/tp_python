#! /usr/bin/env python
# -*-coding:UTF-8 -*-
# Exo 12 (c) 2019

## Import des librairies
from os import path
import pickle

## Declarations
def createPlayer(player, scores):
    if player in scores.keys():
        print("player {} already exists\n". format(player))
    else:
        scores[player] = 0
        print('player {} created\n'.format(player))

def delPlayer(player, scores):
    if player in scores.keys():
        del scores[player]
        print('player {} deleted\n'.format(player))
    else:
        print("player {} already exists\n". format(player))

#debugage
#import pdb; pdb.set_trace()

def getScore(player, scores):
    if player in scores.keys():
        return scores[player]
    else:
        print("player {} not found\n". format(player))
        return False

def setScore(player, score, scores):
    if player in scores.keys():
        scores[player] = score
    else:
        print("player {} not found\n". format(player))
        return False

def loadScore(f_name):
    if (file_exists(f_name)):
        try:
            with open(f_name, 'r') as fichier:
                mon_depickler = pickle.Unpickler(fichier)
                scores = mon_depickler.load()
                fichier.close()
        except FileError:
            print('File error on {}'.format(f_name))
    else:
        scores = dict()

    return scores

def saveScore(scores, f_name):
    try:
        with open(f_name, 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(scores)
            fichier.close()
    except FileError:
        print('File error on {}'.format(f_name))

def file_exists(f_name):
    return path.exists(f_name)

#fileScores = "scores.data"
#if __name__ == "__main__":
#    pscores = loadScore(fileScores)
#    print type(pscores)
#    getScore('riri', pscores)
#    createPlayer('riri', pscores)
#    createPlayer('toto', pscores)
#    setScore('riri', 10, pscores)
#    saveScore(pscores, fileScores)
