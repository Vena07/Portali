import random
import time
print("Had a žebřík")
pole = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "]

hrac1pole= 0
hrac2pole= 0

dolu = [7,22]
nahoru = [2,6,11,17]

def Dolu():
    global hrac1pole,hrac2pole,dolu,nahoru
    if hrac1pole in dolu or hrac1pole in nahoru or hrac2pole in dolu or hrac2pole in nahoru:
        if hrac1pole == 7:
            pole[7] = " " 
            pole[3]= "☻"
        if hrac1pole == 22:
            hrac1pole = 13    

def Hrac1():
    global hrac1, hrac1pole , hod
    hrac1 = "☻"
    hrac1pole += 1

def Hrac2():
    global hrac2, hrac2pole , hod
    hrac2 = "☺"
 

def Hra():
    global pole
    print(f"  ")
    print(f"┌─┬─┬─┬─┐")
    print(f"│{pole[20]}│{pole[21]}│{pole[22]}│{pole[23]}│")
    print(f"├─┼─┴─┴─┘")    
    print(f"│{pole[19]}│↑ ↓")    
    print(f"├─┼─┐↓┌─┐")    
    print(f"│{pole[18]}│{pole[17]}│↓│{pole[16]}│")
    print(f"└─┴─┘↓├─┤")    
    print(f" ↑   ↓│{pole[15]}│")
    print(f"┌─┬─┬─┼─┤")
    print(f"│{pole[11]}│{pole[12]}│{pole[13]}│{pole[14]}│")
    print(f"├─┼─┴─┴─┘")    
    print(f"│{pole[10]}│    ↑") 
    print(f"├─┼─┬─┬─┐")
    print(f"│{pole[9]}│{pole[8]}│{pole[7]}│{pole[6]}│")
    print(f"└─┴─┴─┼─┤")
    print(f"   ↑ ↓│{pole[5]}│")
    print(f"┌─┬─┬─┼─┤")
    print(f"│{pole[1]}│{pole[2]}│{pole[3]}│{pole[4]}│")
    print(f"└─┴─┴─┴─┘")    
Hra()
dobry = False


while True:
    while dobry == False:
        hod = input("Poro hození kostkou napište 1: ")
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

    print(f"Hodil jste:{hod}")
    time.sleep(2)    
    for i in range(hod):
        Hrac1()
        pole[hrac1pole] = hrac1

        smazanipole = hrac1pole - 1
        pole[smazanipole] = " "
        Hra()
        time.sleep(0.5)
    Dolu()