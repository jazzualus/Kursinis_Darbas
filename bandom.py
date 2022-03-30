from tkinter import *
from PIL import Image, ImageTk
import random
from random import randint
import time
import os
import sys
import subprocess

root = Tk()
root.eval('tk::PlaceWindow . center')
root.title('Atmintis')
root.geometry("422x422")
meniu = Menu(root)
root.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)

def close():
    root.destroy()

def is_naujo():
    root.destroy()
    subprocess.call(["python", os.path.join(sys.path[0], __file__)] + sys.argv[1:])

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Paleisti is naujo", command=is_naujo)
submeniu.add_command(label="Uzdaryti programa", command=close)


#aprasomas eiluciu ir stulpeliu kiekis
root.columnconfigure(0, weight=1,)
root.columnconfigure(1, weight=1,)
root.columnconfigure(2, weight=1,)
root.columnconfigure(3, weight=1,)
root.rowconfigure(0, weight=1,)
root.rowconfigure(1, weight=1,)
root.rowconfigure(2, weight=1,)
root.rowconfigure(3, weight=1,)

#priskiriami paveiksliukai
photo1 = Image.open("hounter.jpg")
photo2 = Image.open("dragon.png")
photo3 = Image.open("tom.png")
photo4 = Image.open("snake.png")
photo5 = Image.open("nelson.png")
photo6 = Image.open("peper.png")
photo7 = Image.open("cow.png")
photo8 = Image.open("donald.jpg")
photo9 = Image.open("klaustukas.png")

#sudaromas paveiksliuku sarasas
photos = [photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9]

#paveiksliukai cikle apkarpomi
for i in range(9):
    locals()["p" + str(i+1)] = photos[i].resize((100, 100))

img1 = ImageTk.PhotoImage(p1)
img2 = ImageTk.PhotoImage(p2)
img3 = ImageTk.PhotoImage(p3)
img4 = ImageTk.PhotoImage(p4)
img5 = ImageTk.PhotoImage(p5)
img6 = ImageTk.PhotoImage(p6)
img7 = ImageTk.PhotoImage(p7)
img8 = ImageTk.PhotoImage(p8)
klaustukas = ImageTk.PhotoImage(p9)


img = [img1, img2, img3, img4, img5, img6, img7, img8, img1, img2, img3, img4, img5, img6, img7, img8]

knopkes = []
atsitiktiniai = [] #paveiksliukai sudedami i sarasa atsitiktine tvarka
numeris = -1

#sukamas ciklas cikle kad sugeneruoti mygtuku matrica(koordinates) ir priskirti mygtukams atsitiktinius paveiksliukus
for i in range(4):
    for y in range(4):
        numeris +=1
        z = random.choice(img)
        atsitiktiniai.append(z)
        knopkes.append(Button(root, image=z, ))
        img.remove(z)
        knopkes[numeris].grid(row=i, column=y)
    print(knopkes)

#funkcija sukuria mygtukus be paveiksliuku
def be_paveiksliuku():
    numeris = -1
    for i in range(4):
        for y in range(4):
            numeris +=1
            knopkes[numeris].configure(image=klaustukas, command=lambda x=numeris: atverti_paveiksliuka(x)) #perduoda kitai funkcijai kuris mygtukas paspaustas
            knopkes[numeris].grid(row=i, column=y)

#praejus nustatytam laikui nuo programos paleidimo mygtuku paveiksliukai pakeiciami tusciais mygtukais
root.after(3500, be_paveiksliuku)


#skaiciuojam paspaudimus
skaicius = 0
skaicius1 = 0
paspaudimai = []
def atverti_paveiksliuka(spaudziam):
    global skaicius, skaicius1
    if knopkes[spaudziam].cget('relief') == RAISED:
        skaicius += 1
        skaicius1 +=1
        #paspaudus mygtukas idumba ir parodomas paveiksliukas
        knopkes[spaudziam].configure(relief=SUNKEN, image=atsitiktiniai[spaudziam], width=100, height=100)
        #isirasom paspaudimus i sarasa
        paspaudimai.append(spaudziam)
        #jeigu paspausti 3 mygtukai imames veiksmu:
        if skaicius1 >2:
            if  knopkes[paspaudimai[skaicius-2]].cget('image') != knopkes[paspaudimai[skaicius-3]].cget('image'):
                knopkes[paspaudimai[skaicius-2]].configure(relief=RAISED, image=klaustukas)
                knopkes[paspaudimai[skaicius-3]].configure(relief=RAISED, image=klaustukas)
                skaicius1 -=2
            else:
                skaicius1 -=2

mainloop()

