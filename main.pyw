#! /usr/bin/python3
#neighbors = {(0,1), (1,0), (0,-1), (-1,0), (-1,1), (1,-1)}

from tkinter import *
joueur = 0
class Case(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self.colors=['green', 'blue']
        self.value = 42

    def flip(self):
        global joueur
        self.value = joueur
        joueur = (joueur + 1) % 2
        self.changeValue()

    def getValue(self):
        return self.value

    def changeValue(self):
        self['bg'] = self.colors[self.value]
        self['state'] = DISABLED

def clic(x, y):
    global joueur
    if buttons[str(x)+"_"+str(y)]["state"] != DISABLED:
        main_text["text"] = "Tour du joueur "+str(((joueur+1)%2)+1)
        buttons[str(x)+"_"+str(y)].flip()
        if verifGagnant(((joueur+1)%2)):
            main_text["text"] = "Joueur "+str(((joueur+1)%2)+1)+" gagne la partie"
            for button in buttons.items():
                buttons[button[0]]['state'] = DISABLED


def verifGagnant(joueur):
    chemin = []
    gagnant = False
    if joueur == 0:
        depart = (0,0)
        finaux = boutons_finaux_j1
    else:
        depart = (0,0)
        finaux = boutons_finaux_j2
    chemin.append(depart)
    for (x,y) in chemin:
        for (a, b) in {(0,1), (1,0), (0,-1), (-1,0), (-1,1), (1,-1)}:
            if (x+a >= 0) and (x+a < nrows) and (y+b >= 0) and (y+b < ncols):
                if buttons[str(x+a)+"_"+str(y+b)].getValue() == joueur:
                    if ((x+a),(y+b)) not in chemin:
                        chemin.append(((x+a),(y+b)))
    for fin in finaux:
        if fin in chemin:
            gagnant = True
    if gagnant:
        return gagnant


ncols = 10
nrows = 10
buttons = {}
boutons_finaux_j1 = []
boutons_finaux_j2 = []
fen = Tk()
fen.title('Grille hexa')
fen.geometry('400x400')
for i in range(nrows):
    for j in range(ncols):
        if(i == 0 or i == (nrows - 1)):
            buttons[str(i)+"_"+str(j)] = Case(fen, text ='', command = lambda i=i,j=j: clic(i,j), bg = 'green', state = DISABLED)
            buttons[str(i)+"_"+str(j)].value = 0
            if i == (nrows - 1):
                boutons_finaux_j1.append((i,j))
        else:
            if(j == 0 or j == (ncols - 1)):
                buttons[str(i)+"_"+str(j)] = Case(fen, text ='', command = lambda i=i,j=j: clic(i,j), bg = 'blue', state = DISABLED)
                buttons[str(i)+"_"+str(j)].value = 1
                if j == (ncols - 1):
                    boutons_finaux_j2.append((i,j))
            else:
                buttons[str(i)+"_"+str(j)] = Case(fen, text ='', command = lambda i=i,j=j: clic(i,j))
        buttons[str(i)+"_"+str(j)].place(x=((25*j)+((i+1)*12.5)), y=25*(i+1))
Label(fen, text = "Joueur 1", fg = "green").place(x = 25, y = 25*(nrows+2))
Label(fen, text = "Joueur 2", fg = "blue").place(x = 25, y = 25*(nrows+4))
main_text = Label(fen, text = "Tour du joueur 1")
main_text.place(x = 150, y = 25*(nrows+3))
fen.mainloop()