from operator import ne
import random

def casino(karty, hodnotacasina):
    if hodnotacasina >= 16:
        print("casino má", hodnotacasina)

    else:
        a = random.choice(karty)
    hodnotacasina += a
    if hodnotacasina > 21:
        print("casino má", hodnotacasina)
        print("je přes!, vyhrál jsi")
        exit()
    if hodnotacasina <= 21:
        print("casino má", hodnotacasina)

    return hodnotacasina
    



def dalsikarta(karty, hodnota, hodnotacasina):
    a = random.choice(karty)
    hodnota += a
    hodnotacasina = casino(karty, hodnotacasina)
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
        if hodnota > hodnotacasina:
            print("vyhrál jsi")
            exit()
        else:
            print("remíza")   
            exit()
    return hodnota, hodnotacasina


def porovnej(hodnota, hodnotacasina):
    if hodnota > hodnotacasina:
        print("vyhrál jsi")
    if hodnota == hodnotacasina:
        print("remíza")
    if hodnota < hodnotacasina:
        print("prohrál jsi")   

def cobudedal(karty, hodnota, hodnotacasina):
    print("chceš další?")
    a = input()
    if a == "ne":
        print("celkem máš ", hodnota)
        print("casino má", hodnotacasina)
        porovnej(hodnota, hodnotacasina)
    if a == "ano":
        (hodnota, hodnotacasina) = dalsikarta(karty, hodnota, hodnotacasina)
        cobudedal(karty, hodnota, hodnotacasina)

karty = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]

(prvni, prvnicasina) = dalsikarta(karty, 0, 0)
cobudedal(karty, prvni, prvnicasina)
