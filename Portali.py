import random
import time
print("Had a žebřík")
pole = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]

portali = []

hrac1pole= 0
hrac2pole= 0


def Hrac1():
    global hrac1, hrac1pole , hod
    hrac1 = "☻"
    hrac1pole += 1

def Hrac2():
    global hrac2, hrac2pole , hod
    hrac2 = "☺"
    hrac2pole += 1
def generace_portalu():
    global portali,pole
    portal = random.randint(2,23)
    portali.append(portal)
    pole[portal] = "O"

def Portal2():
    global  hrac2pole,portali,pole
    if hrac2pole in portali:
        pole[hrac2pole] = "O"
        presun = random.choice(portali)
        pole[presun] =  "☺"
        hrac2pole = presun

def Portal1():
    global  hrac1pole,portali,pole
    if hrac1pole in portali:
        pole[hrac1pole] = "O"
        presun = random.choice(portali)
        pole[presun] =  "☻"
        hrac1pole = presun


def Hra():
    global pole
    print(f"  ")
    print(f"┌─┬─┬─┬─┐")
    print(f"│{pole[21]}│{pole[22]}│{pole[23]}│{pole[24]}│")
    print(f"├─┼─┴─┴─┘")    
    print(f"│{pole[20]}│")    
    print(f"├─┼─┬─┬─┐")    
    print(f"│{pole[19]}│{pole[18]}│{pole[17]}│{pole[16]}│")
    print(f"└─┴─┴─┼─┤")    
    print(f"      │{pole[15]}│")
    print(f"┌─┬─┬─┼─┤")
    print(f"│{pole[11]}│{pole[12]}│{pole[13]}│{pole[14]}│")
    print(f"├─┼─┴─┴─┘")    
    print(f"│{pole[10]}│    ") 
    print(f"├─┼─┬─┬─┐")
    print(f"│{pole[9]}│{pole[8]}│{pole[7]}│{pole[6]}│")
    print(f"└─┴─┴─┼─┤")
    print(f"      │{pole[5]}│")
    print(f"┌─┬─┬─┼─┤")
    print(f"│{pole[1]}│{pole[2]}│{pole[3]}│{pole[4]}│")
    print(f"└─┴─┴─┴─┘")    

dobry = False
pocet = random.randint(6,10)

for i in range(pocet):
    generace_portalu()
Hra()
while True:
    
    while dobry == False:
        hod = input("hraáči1, Pro hození kostkou napište 1: ")
        try:
            hod = int(hod)
            if hod == 1:
                dobry = True
            else:
                print("Zdali jste špatnou hodnotu!!")
        except ValueError:
            print("Zdali jste špatnou hodnotu!!")
    dobry = False
    
    hod = random.randint(1,6)

    print(f"hrači1 Hodil jste:{hod}")
    time.sleep(2)    
    for i in range(hod):
        Hrac1()
        pole[hrac1pole] = hrac1

        smazanipole = hrac1pole - 1
        test = hrac1pole -1        
        if smazanipole in portali:
            pole[smazanipole] = "O"
        elif hrac2pole == test and 0<i<hod:
            pole[smazanipole] = "☺"
        
        else:
            pole[smazanipole] = " "
        
       
       
        if hrac1pole==24:
            print("Hrac1 výtezí!!!")
            time.sleep(100)
        
        Hra()
        time.sleep(0.5)
    Portal1()
    Hra()

    
    while dobry == False:
        hod = input("hráči2, Pro hození kostkou napište 1: ")
        try:
            hod = int(hod)
            if hod == 1:
                dobry = True
            else:
                print("Zdali jste špatnou hodnotu!!")
        except ValueError:
            print("Zdali jste špatnou hodnotu!!")
    dobry = False
    
    hod = random.randint(1,6)

    print(f"hrači2 Hodil jste:{hod}")
    time.sleep(2)    
    for i in range(hod):
        Hrac2()
        pole[hrac2pole] = hrac2
        test = hrac2pole -1
        smazanipole = hrac2pole - 1
        if smazanipole in portali:
            pole[smazanipole] = "O"
        elif hrac1pole == test and 0<i<hod:
            pole[smazanipole] = "☻"
        else:
            pole[smazanipole] = " "
        
        if hrac2pole==24:
            print("Hrac2 výtezí!!!")
            time.sleep(100)
        
        Hra()
        time.sleep(0.5)
    Portal2()
    Hra()    