
from tkinter import * 
from pandas import DataFrame # type: ignore
from PIL import Image , ImageTk
from Info import getInfo_with_interface
import mysql.connector  # type: ignore
db = mysql.connector.connect(
          host= "localhost",
          user= "ousmane",
          password ="ousmane@Mysql", 
          database = "projetexamen"
)
isAuthentificated = False
def authentification(): # authentification des utilisateurs en fournissant leur login et leur mot de passe 
         global isAuthentificated
         user = input_user.get() 
         password = input_password.get()
         cursor = db.cursor()
         cursor.execute("select * from utilisateur where login =%s and password =%s" ,(user , password))
         rows =  cursor.fetchall()
         if  not len(rows) > 0:
               labelInfo["text"]  = "Désolé , login ou mot de passe invalide 🤦‍♂️ "
               labelInfo["fg"] ="red"
         else:
                   labelInfo["text"] = "Authentification reussi ✨"
                   isAuthentificated = True
                   frame_authentification.pack_forget()
                   frame1.pack(padx =20  , pady =50)
                        
                   
                   
def show(target): # afficher la liste des utilisateurs/chauffeurs/receveurs/bus : en fonction de la target
          # definir un tableau qui doit contenir la liste 
          liste  =[]
          cursor = db.cursor()
          cursor.execute(f'show columns from {target}')
          columns =[column[0] for column in cursor.fetchall()]
          cursor.execute(f"select * from {target}")
          rows= cursor.fetchall()
          for row in rows:
                liste.append(list(row))  
          dataframe = DataFrame(liste, columns = columns)     
          frame = Frame() 
          text_widget = Text(master =frame ,wrap=None) 
          text_widget.insert(INSERT, dataframe.to_string(index = False))
          text_widget.pack(fill = BOTH , expand =True)
      #     scrolbar = Scrollbar(master = text_widget ,orient= VERTICAL)
      #     scrolbar.pack(side = "right" , fill= "y")    
          frame.pack()
          
          
                                                  

                               
def delete(target):# supprimer des utilisateurs/chauffeur/bus/receveurs : en fonction de la target
          cursor = db.cursor()
          cursor.execute(f"delete from {target}")
def add(target):
     
     if target == "utilisateur" :
          frame_crud_users.pack_forget()
          frame_info_user.pack()
          nom = input_nom_user.get()
          prenom= input_prenom_user.get()
          mail = input_mail_user.get()
          login = input_login_user.get()
          password = input_password_user.get()
          button = Button(master= fenetre , text = "valider" , background ="orange" ,
                          command= lambda: adduser(nom ,prenom ,mail ,login ,password))
          button.pack()
                       
           
def adduser(nom , prenom,mail , login ,password):
      cursor= db.cursor()
      requeste = f"select* from user where login ={login} and password ={password}"
      cursor.execute(requeste)
      rows = cursor.fetchall()
      if rows != None:
            try:
                  cursor.execute(f"insert into utilisateur ('nom','prenom','mail','login',password') values({nom} ,{prenom} ,{mail},{login}, {password})")
            except:
                  print("impossible de faire un ajout")
      else:
            Label(master= fenetre , text= "operation impossible ,l'utilisateur exsiste déja !", fg = "red" , font = 10).pack()          
def update(target): # modifier un utilisateur/chauffeur/receveurs/bus : en fonction de la target 
         pass
        
def show_frame_crud_users():
      frame_authentification.pack_forget()
      frame1.pack_forget()
      frame_crud_users.pack(padx =20 , pady =20 )
def show_frame_crud_drivers():
      frame_authentification.pack_forget()
      frame1.pack_forget()
      frame_crud_drivers.pack(padx =20 , pady =20 )

def show_frame_crud_receivers():
      frame_authentification.pack_forget()
      frame1.pack_forget()
      frame_crud_receivers.pack(padx =20 , pady =20 )
      
fenetre = Tk()
fenetre.geometry("900x600")
fenetre.title("Gestion de bus - Interface utilisateur")
fenetre.resizable(width = False , height= False)
fenetre.attributes('-alpha' ,0.9)
# definir une image de background pour notre fenetre
bg_image = Image.open("bus.png")
bg_image = bg_image.resize((900, 600))
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = Label(fenetre, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# frame d'authentification
frame_authentification  =  Frame(master = fenetre , bg = 'white' , padx =20 , pady =20)
frame_authentification.pack(padx =20, pady=20)#place(relx =0.5 , rely =0.5 , anchor=CENTER) 
# information d'acceuil sur la page 
labelInfo = Label(master = frame_authentification, 
              bg = "blue" ,
              border =5,
               justify= "center"  , 
               width =400,
               text= "Veuillez vous authentifier! ✔", height=3 , 
              fg ="black" ,
              font=("Helvetica",16,"bold")
              )
labelInfo.pack( pady=20)
label_user = Label(master = frame_authentification, 
                   bg = 'white' , 
                   justify= "center" ,
                   text ="Nom d'utilisateur" ,
                   font =("Arial",12)
                   )
label_user.pack( padx = 10) 
input_user = Entry( master = frame_authentification , width =30, font =("Arial",12) , justify= "center")
input_user.pack( pady =5)
# definition des elements pour les motsde passe !
label_password = Label(master = frame_authentification , 
                   bg = 'white' , 
                   justify= "center" ,
                   text ="Mot de passe" ,
                   font=("Arial" ,12)
                   )
label_password.pack( pady=10 ) 
# password = StringVar()
input_password = Entry( master = frame_authentification , 
                       width=30 , 
                       font =("Arial",12) ,
                       justify= "center" ,
                       show ="*" )
input_password.pack( pady=5)
button = Button( master = frame_authentification , 
                text = "Connexion"  ,
                justify="center" ,
                width = 15 , height=2  ,
                bg = "orange", 
                fg ="white" ,
                font =("Arial" ,12 ,"bold"),
                command= authentification )
button.pack( pady=20 )


# label_image =Label(master= fenetre, image= image).pack(side ="bottom")
# label_image.pack()
# fenetre.image = image ##### ajouter une image à notre fenetre principale 

############## utilisation d'une  autre frame aprés authentification de l'utilisateur #####################
frame1 = Frame(master = fenetre  ,padx =20 ,pady =20 )
text_bienvenu = Label(master = frame1, 
               bg = "pink" ,
               justify= "center"  , 
               width =400,
               text= "Bienvenu sur l'application de gestion de bus😍😍❤", height=5 , 
              font =("helvetica",16 ,"bold") ,
              border =5 , fg = "black" 
              )
text_bienvenu.pack( pady =20 )
def create_button_with_text(frame,  command ,justify = "center" ,text="" , info ="" ):
      subframe  = Frame(master=  frame ,padx =10 , pady=3  , width= 300 )
      Button(master = subframe ,  width =40 , height=3 ,
                      fg ="black", 
                      text = text ,justify = justify,
                      font =("Arial",12, "bold"),
                      command= command).pack(padx =10 , pady = 5 , side = "left" ) # 
      Label(master = subframe , border =1 ,text = info ,font =("Arial",12 ,"bold"),fg = "blue" ,
            height=3 ).pack(side ="right")
      subframe.pack()
      
create_button_with_text(frame1  ,
                            show_frame_crud_users ,text= "Gestion des utilisateurs", info= """vous pouvez ajouter, \n supprimer ou modifiers  👀""" )
create_button_with_text(frame1  ,  show_frame_crud_drivers  , info =  """vous pouvez ajouter, \nsupprimer ou modifiers 👀"""
                        , text=  "Gestion des chauffeurs"
                        )
create_button_with_text(frame1  ,
                        show_frame_crud_receivers , text= "Gestion des chauffeurs" , info= """vous pouvez ajouter,\nsupprimer  ou modifiers  👀"""
                        )
create_button_with_text(frame1  ,
                        show_frame_crud_receivers , text= "Gestion des Bus" , info= """vous pouvez ajouter,\nsupprimer  ou modifiers  👀"""
                        )

def create_frame_with_crud(master = fenetre , text_from = ""):
      frame = Frame(master = master )
      create_button_with_text(frame  , 
                              lambda: add(text_from), text =" ajouter "+text_from)
      create_button_with_text(frame  , 
                              lambda: show(text_from)
                                    
                              , text= "afficher la liste des "+text_from+"s") #  afficher une liste(utilisateurs , receveurs ..)
      create_button_with_text(frame  ,
                              lambda: delete(text_from) 
                              , text= "supprimer des "+ text_from+"s") # mettre à jour des informations(utilisateurs ,  chauffeurs ,..)
      create_button_with_text(frame  ,
                              lambda: update(text_from)
                              ,text = "mettre à jour des "+text_from+"s") #  supprimer des informations 
      return frame
      
################### frame pour les operations de  type CRUD ######################""
      ## pour les  utilisateurs  sur la base de données ###
frame_crud_users  =create_frame_with_crud(text_from = "utilisateur")
############ pour les chauffeurs #########"""
frame_crud_drivers = create_frame_with_crud(text_from = "chauffeur")
######"" pour les receveurs #######"
frame_crud_receivers = create_frame_with_crud(text_from = "receveur")
### pour les bus ##""
frame_crud_receivers = create_frame_with_crud(text_from = "bus")
#################### interface pour l'ajout la suppression et modification des utilisateurs ###############
frame_info_user = Frame(fenetre , width=500 ,padx =10 , pady=20  )
label_nom_user = Label(master = frame_info_user, 
                   justify= "center" ,
                   text ="Nom" ,
                   font =("Arial",12),
                   width= 30
                   )
label_nom_user.pack( padx = 10) 
input_nom_user = Entry( master = frame_info_user , width =30, font =("Arial",12) , justify= "center")
input_nom_user.pack( pady =5)
label_prenom_user = Label(master = frame_info_user,  
                        justify= "center" ,
                        text ="Prenom" ,
                        font =("Arial",12),
                        width= 30
                        )
label_prenom_user.pack(padx =10)
            
input_prenom_user = Entry( master = frame_info_user , width =30, font =("Arial",12) , justify= "center")
input_prenom_user.pack( pady =5)
label_mail_user = Label(master = frame_info_user, 
                        justify= "center" ,
                        text ="E-mail" ,
                        font =("Arial",12),
                        width= 30
                        )
label_mail_user.pack(padx =10)
            
input_mail_user = Entry( master =frame_info_user , width =30, font =("Arial",12) , justify= "center")
input_mail_user.pack( pady =5)

label_login_user= Label(master =frame_info_user, 
                        justify= "center" ,
                        text ="Login" ,
                        font =("Arial",12),
                        width= 30
                        )
label_login_user.pack(padx =10)
            
input_login_user = Entry( master =frame_info_user , width =30, font =("Arial",12) , justify= "center")
input_login_user.pack( pady =5)

label_password_user = Label(master = frame_info_user, 
                        justify= "center" ,
                        text ="Password" ,
                        font =("Arial",12),
                        width= 30 
                        )
label_password_user.pack(padx =10)
            
input_password_user= Entry( master = frame_info_user , width =30, font =("Arial",12) , justify= "center" , show ="*")
input_password_user.pack( pady =5)
#######################" interface pour l'ajout  , la suppression et le mise à jour des informations sur les chauffeurs "#####################""
frame_info_chauffeur = Frame(fenetre , width=200 ,padx =10 , pady=20 )
label_nom_chauffeur = Label(master = frame_info_chauffeur, 
                   justify= "center" ,
                   text ="Nom" ,
                   font =("Arial",12),
                   width= 30
                   )
label_nom_chauffeur.pack( padx = 10) 
input_nom_chauffeur = Entry( master = frame_info_chauffeur , width =30, font =("Arial",12) , justify= "center")
input_nom_chauffeur.pack( pady =5)
label_prenom_chauffeur = Label(master = frame_info_chauffeur,  
                        justify= "center" ,
                        text ="Prenom" ,
                        font =("Arial",12),
                        width= 30
                        )
label_prenom_chauffeur.pack(padx =10)
input_prenom_chauffeur = Entry( master = frame_info_chauffeur, width =30, font =("Arial",12) , justify= "center")
input_prenom_chauffeur.pack( pady =5)
label_telephone_chauffeur = Label(master = frame_info_chauffeur, 
                        justify= "center" ,
                        text ="Telephone" ,
                        font =("Arial",12),
                        width= 30
                        )
label_telephone_chauffeur.pack(padx =10)
input_telephone_chauffeur = Entry( master = frame_info_chauffeur , width =30, font =("Arial",12) , justify= "center")
input_telephone_chauffeur.pack( pady =5)
label_age_chauffeur = Label(master = frame_info_chauffeur, 
                        justify= "center" ,
                        text ="Age" ,
                        font =("Arial",12),
                        width= 30
                        )
label_age_chauffeur.pack(padx=10)
input_age_chauffeur = Entry( master = frame_info_chauffeur , width =30, font =("Arial",12) , justify= "center")
input_age_chauffeur.pack( pady =5)
label_permis_chauffeur = Label(master = frame_info_chauffeur, 
                        justify= "center" ,
                        text ="Permis(A ou B)" ,
                        font =("Arial",12),
                        width= 30
                        )
label_permis_chauffeur.pack(padx=10)
input_permis_chauffeur = Entry( master = frame_info_chauffeur , width =30, font =("Arial",12) , justify= "center")
input_permis_chauffeur.pack( pady =5)
######################## interface pour l'ajout , la  suppresion et la modification des receveurs #######################
frame_info_receveur = Frame(fenetre , width=200 ,padx =10 , pady=20 )
label_nom_receveur = Label(master = frame_info_receveur, 
                   justify= "center" ,
                   text ="Nom" ,
                   font =("Arial",12),
                   width= 30
                   )
label_nom_receveur.pack( padx = 10) 
input_nom_receveur = Entry( master = frame_info_receveur , width =30, font =("Arial",12) , justify= "center")
input_nom_receveur.pack( pady =5)
label_prenom_receveur = Label(master = frame_info_user, 
                        justify= "center" ,
                        text ="Prenom" ,
                        font =("Arial",12),
                        width= 30
                        )
label_prenom_receveur.pack(padx =10)
input_prenom_receveur= Entry( master = frame_info_receveur , width =30, font =("Arial",12) , justify= "center")
input_prenom_receveur.pack( pady =5)
label_telephone_receveur= Label(master = frame_info_receveur, 
                        justify= "center" ,
                        text ="Telephone" ,
                        font =("Arial",12),
                        width= 30
                        )
label_telephone_receveur.pack(padx =10)
input_telephone_receveur = Entry( master = frame_info_receveur , width =30, font =("Arial",12) , justify= "center")
input_telephone_receveur.pack( pady =5)
label_age_receveur = Label(master = frame_info_receveur,  
                        justify= "center" ,
                        text ="Age" ,
                        font =("Arial",12),
                        width= 30
                        )
label_age_receveur.pack(padx=10)
input_age_receveur = Entry( master = frame_info_receveur, width =30, font =("Arial",12) , justify= "center")
input_age_receveur.pack( pady =5)



fenetre.mainloop()


          



