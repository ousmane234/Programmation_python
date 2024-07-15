from random import randrange
import tkinter as tk 
side = 400
fenetre = tk.Tk()
can = tk.Canvas(fenetre , width =500 , height = 500 ,bg ="grey")
can.pack()
def show() :
	center  = (randrange(side)  , randrange(side))
	can.create_image(center , image = tk.PhotoImage(file = "logo.jpeg"))

# creation d'un bouton qui fera  apparaitre notre image sur la canvas
tk.Button( fenetre , text = "Show_Image", command = show, bg ="blue").pack()
fenetre.mainloop() # lancer l'ecouteur d'evenement

