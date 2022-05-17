from operator import ne
import random

def dalsikarta(karty, hodnota):
    a = random.choice(karty)
    hodnota += a
    if hodnota > 21:
        print("dostal jsi ", a)
        print("celkem máš ", hodnota)
        print("jsi přes!")
        exit()
    if hodnota < 21:
        print("dostal jsi ", a)
        print("celkem máš ", hodnota)
    if hodnota == 21:
        print("dostal jsi ", a)
        print("celkem máš ", hodnota)
        print("vyhrál jsi")
        exit()
    return hodnota

def porovnej(hodnota):
    if hodnota > 16:
        print("vyhrál jsi")
    if hodnota == 16:
        print("remíza")
    if hodnota < 16:
        print("prohrál jsi")   

def cobudedal(karty, hodnota):
    print("chceš další?")
    a = input()
    if a == "ne":
        print("celkem máš ", hodnota)
        print("dealer má 16")
        porovnej(hodnota)
    if a == "ano":
        hodnota = dalsikarta(karty, hodnota)
        cobudedal(karty, hodnota)

karty = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

prvni = dalsikarta(karty, 0)
cobudedal(karty, prvni)
