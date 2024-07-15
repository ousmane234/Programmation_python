#######################"" LE DAMIER ################################# 
import tkinter as tk
from random import randrange
def damier(): # Representation d'un damier  sur deux couleurs
	couleurs = ["blue" , "white"]
	rect = can.create_rectangle(5, 5 ,500 ,500 )
	for i in range(10):
		for  j in range(10):
			can.create_rectangle(5+50*j ,5+50*i , 5+50*(j+1) ,5+50*(i+1) , fill = couleurs[(j+i)%2])

global SIDE

def tracer_cercle ( x ,y , r , couleur = "red"):
	can.create_oval( x-r , y-r ,x+r , y+r , fill = couleur)

def pion ():
	tracer_cercle(5+50*(randrange(10))+25 , 5+ 50*(randrange(10))+25 , 10)
def show ():
	center =(randrange(SIDE) , randrange(SIDE)) 
	can.create_image( center , image = tk.PhotoImage(file = "logo.png"))

fenetre = tk. Tk()
fenetre.geometry("700x700+50+50")
can = tk.Canvas( fenetre , width =  500 ,  height= 500 , bg = "grey")
tk.Label( fenetre , text = "jeu de damier").pack()
can.pack( side = "top" , padx =5 , pady = 5) # methode : faire appraitre le widget sur le parent
tk.Button( fenetre , text ="Quitter" , fg = "red" , command = fenetre.destroy ).pack(side = "right"  ,padx = 5 , pady  = 5 )
tk.Button ( fenetre , text ="Damier" , fg = "blue"  , command = damier ).pack( side = "left" ,padx = 5 , pady = 5)
tk.Button ( fenetre , text = "placer_pion" , fg = "green" , command = pion).pack( padx= 5)
print(fenetre.winfo_screenwidth() ,fenetre.winfo_screenheight() ,fenetre.winfo_geometry())
# fenetre.mainloop() # lancer l'ecouteur d'evenement
# logo = tk.PhotoImage(file = "./logo.png")
fenetre.mainloop()




			



	
