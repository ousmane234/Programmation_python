
from tkinter import * 
from pandas import DataFrame # type: ignore
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
         else:
                   labelInfo["text"] = "Authentification reussi ✨"
                   isAuthentificated = True
                   frame_authentification.pack_forget()
                   frame1.pack(padx =10  , pady =100)
                        
                   
                   
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
          
def update(target): # modifier un utilisateur/chauffeur/receveurs/bus : en fonction de la target 
         pass
        
def show_frame_crud_users():
      frame1.pack_forget()
      frame_crud_users.pack(padx =10 , pady =20 )
def show_frame_crud_drivers():
      frame1.pack_forget()
      frame_crud_drivers.pack(padx =10 , pady =20 )

def show_frame_crud_receivers():
      frame1.pack_forget()
      frame_crud_receivers.pack(padx =10 , pady =20 )
      
fenetre = Tk()
fenetre.geometry("900x1000")
fenetre.resizable( width=  True , height= False)
frame_authentification  =  Frame(master = fenetre , bg = 'gray')
frame_authentification.pack(side ="top" , padx =10 , pady =10 ) # side ="top" ,pady =10 ,padx =10 ,
labelInfo = Label(master = frame_authentification, 
              bg = "blue" ,
              border =5,
               justify= "center"  , 
               width =700,
               text= "Veuillez vous authentifier! ✔", height=5 , 
              fg ="coral" ,
              font= 70
              )
labelInfo.pack( padx =100, pady=50)
label_user = Label(master = frame_authentification, 
                   bg = 'aqua' , 
                   justify= "center" ,
                   text =" user login" ,
                   width = 30 
                   )
label_user.pack( padx = 90) 
input_user = Entry( master = frame_authentification ,  width=50 , foreground= "blue" , justify= "center")
input_user.pack(after = label_user , padx =90 , pady =[0,10])
# definition des elements pour les motsde passe !
label_password = Label(master = frame_authentification , 
                   bg = 'aqua' , 
                   justify= "center" ,
                   text =" user password" ,
                   width = 30
                   )
label_password.pack( padx = 90 ) 
# password = StringVar()
input_password = Entry( master = frame_authentification , 
                       width=50 , 
                       foreground= "blue" ,
                       justify= "center" ,
                       show ="*" )
input_password.pack(after = label_password , padx =90)
button = Button( master = frame_authentification , 
                text = "Submit"  ,
                justify="center" ,
                width = 15 , height=2  ,
                bg = "orange", 
                command= authentification )
button.pack( padx =100 , pady =[20 ,0] )
image = PhotoImage(file = "transport.jpeg")
Label(master= fenetre, image= image).place()

############## utilisation d'une  autre frame aprés authentification de l'utilisateur #####################
frame1 = Frame(master = fenetre  ,  background= "gray")
text_bienvenu = Label(master = frame1, 
              bg = "pink" ,
              border =5,
               justify= "center"  , 
               width =500,
               text= "Bienvenu sur l'application de gestion de bus😍😍❤", height=5 , 
              fg ="black" ,
              font= 70
              )
text_bienvenu.pack(padx =10 , pady =10 )
def create_button_with_text(frame, color,  command ,justify = "center" ,text="" , info =""):
      subframe  = Frame(master=  frame ,  bg = "gray" ,padx =10 , pady=10 )
      Button(master = subframe ,  width =40 , height=3 ,
                      bg = color ,
                      font =40 , 
                      fg ="blue", 
                      text = text ,justify = justify,
                      command= command).pack(padx =10 , pady =[5,0] , side = "left" ) # 
      Label(master = subframe , border =1 ,text = info ,font =30 ,fg = "blue", bg ="gray",
            height=3 ).pack(side ="right")
      subframe.pack()
      
create_button_with_text(frame1  ,
                          "white" ,  show_frame_crud_users ,text= "Gestion des utilisateurs", info= """vous pouvez ajouter, \n supprimer ou modifiers  👀""" )
create_button_with_text(frame1  , "white" ,  show_frame_crud_drivers  , info =  """vous pouvez ajouter, \nsupprimer ou modifiers 👀"""
                        , text=  "Gestion des chauffeurs"
                        )
create_button_with_text(frame1  , "white" ,
                        show_frame_crud_receivers , text= "Gestion des chauffeurs" , info= """vous pouvez ajouter,\nsupprimer  ou modifiers  👀"""
                        )
create_button_with_text(frame1  , "white" ,
                        show_frame_crud_receivers , text= "Gestion des Bus" , info= """vous pouvez ajouter,\nsupprimer  ou modifiers  👀"""
                        )

def create_frame_with_crud(master = fenetre , text_from = ""):
      frame = Frame(master = master , bg ="gray", width = 70)
      create_button_with_text(frame  , 
                              "white" , 
                              lambda: show(text_from)
                                    
                              , text= "afficher la liste des "+text_from+"s") #  afficher une liste(utilisateurs , receveurs ..)
      create_button_with_text(frame  ,
                              "white",
                              lambda: delete(text_from) 
                              , text= "supprimer des "+ text_from+"s") # mettre à jour des informations(utilisateurs ,  chauffeurs ,..)
      create_button_with_text(frame  ,
                              "white",
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



fenetre.mainloop()


          



