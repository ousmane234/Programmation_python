# """Ecrire un programme  qui demande à l'utilisateur son nom et son année de naissance
# le programme nous informe si l'utilisateur est majeur ou mineur
# NB:Le programme forcera l'utilisateur à donner une valeur numérique pour l'année de naissance
# """
# nom = input("Entrer  votre nom\n")
# annee_naissance = input("entrer votre annnée de naissance\n")
# while(annee_naissance.isnumeric()==False):
#             print("vous devez donner  un nombre pour l'annee\n")
#             annee_naissance = input("ressayer\n")

# age = 2024- int(annee_naissance) 
# if(age>18):
#             print(nom ,"Vous êtes majeur\n")
# else:
#             print( nom,"vous être mineur")            


#             """
#             Exerice2: Ecrie un programme qui demande  à l'utilisateur un verbe
#             le programme nous informe si le verbe est du premier groupe ou pas 
#             """
# verbe = input("Entrer un verbe ") 
# while (verbe.isnumeric()==True):
#         print("vous devez entrer une chaine")
#         verbe = input("Entrer un autre verbe").lower()
# if verbe.endswith("er") and verbe != "aller":
#         print("le verbe", verbe ,"est du premier groupe") 
#         #conjugaison du verbe :
#         terminaisons =["e", "es","e","ons","ez","ent"]
#         pronoms =["Je","Tu","Il/Elle", "Nous","Vous","Ils/Elles"]
#         voyelles =['a','o','u','e']
#         radical = verbe[:len(verbe)-2]
#         for i in range (len(terminaisons)):
#                 print(pronoms[i] , " " ,radical+terminaisons[i])          
              
# else:
#         print(verbe, "n'est pas du premier groupe")
        



############################### COURS 5 : listes , dictionnaires , tuples et ensembles #############################    

# Ecrire une fonction qui permet de calculer la somme des elements d'une liste
# liste = [5,8,9,4,10,0,5]
# somme= 0
# # for element in liste:
# # 	somme += element
# # print("la somme est : ", somme)	

# for i in range( len(liste)):
# 	somme += liste[i]
# print("la somme  est: " , somme)	

# #implentation de la fonction max() pour une liste
# liste1 = [5,8,9,4,10, -1 , - 10 ,0,5]
# maximum =  liste1[0]
# for element in liste1:
# 	if element > maximum :
# 		maximum = element
# print("le maximum de la liste est :", maximum)	
# # implementation de la fonction min() pour une liste
# liste2 = [5,8,9,4,10, -1 , - 10 ,0,5]	
# minimum = liste2[0]
# for element in liste2:
# 	if element < minimum:
# 		minimum = element
# print("le minimum de la liste est ", minimum)
############################################### COURS N°6  les donnnées structurées (listes multidimensionnelles)####################################################
"""Ecrire un programme qui demande à l'utilisateur les information des etudiants d'une classe
 Un etudiant est caractérisé par son nom , prenom , INE , date de naissance
Le programme nous affiche: 
1) tous les etudiants dont leur nom contient a et e
2)Afficher les etudiants agé de plus de 25 ans et que le prenom depasse 6 lettres
"""

"""EX0 : chiffrer et dechiffrer un message en utilisant le  chiffrement de cesar"""
# CHIFFREMENT D'UN MESSAGE PAR CESAR 
# cipher = ""
# lettres = [chr(i) for i in range(ord('a') , ord('z')+1)]
# chiffres = [chiffre for chiffre in range(26)]
# mon_dictionnaire = dict((lettres[i] ,chiffres[i]) for i in range(26))
# while True:
# 	message = input("Entrer un message à chiffrer (chiffrement de Cesar)" )
# 	if message.isalpha() or " " in message :
# 		for lettre in message.lower():
# 			if lettre == " ":
# 				cipher += lettre
# 				continue
# 			c = (mon_dictionnaire.get(lettre) +3)%26
# 			cipher += list(mon_dictionnaire.keys())[c]
# 		print(" le  chiffré de " , message  ,"est " ,cipher) 

# 		break
# 	else:
# 		print("le message ne doit comporter que des lettre")	
# # DECHIFFREMENT D'UN CIPHER PAR CESAR
# while True:
# 	cipher = input("Entrer un message déchifffrer (Cesar)")
# 	clair = ""
# 	if cipher .isalpha() or " " in cipher :
# 		for lettre in cipher.lower():
# 			if lettre ==" ":
# 				message += lettre
# 				continue
# 			m= (mon_dictionnaire.get(lettre) -3)%26
# 			if m < 0:
# 				m += 26
# 			clair  +=  list(mon_dictionnaire.keys())[m]	
# 		print("le déchiffré de "  , cipher ,"est " , message)
# 		break	



 ################################# cours 7 : programmation modulaire et ggestion des exceptions en  python###################""
""" I. Les fonctions en python
	1. Syntaxe et mode d'utilisation
	2. portée des variables  dans une fonctions (variables locales et variables globales)
    II. les modules en python !!!
	1. importation de module ( from nomModule import *    ,,,,, nomModule import fonction1 , fonction1 ,..... ,,,,,,  import module)
    III. la gestion des exceptions en python

""" # exercies sur les modules et les fonnctions :
############################### le chiffrement  et dechiffrement de cesar ##########################

def cesar_cipher (message , cle=3):
          cipher = ""
          for element in message:
                    if(element.islower()):
                              cipher +=chr((ord(element)-97 +cle)%26 + 97)
                    elif( element.isupper()):
                              cipher += chr((ord(element)-65 +cle)%26 + 65)
                    else:
                              cipher += element
          return cipher    
def dechiffrement( chiffre , cle):
            message =""
            for element in chiffre:
                    if(element.islower()):
                             message += chr((ord(element) -97 -cle)%26 +97)
                    elif(element.isupper()):
                            message += chr((ord(element)-65 -cle)%26 +65)
                    else:
                            message+= element
                            
            return message       
# def brute_force(cipher):
#     message = ""
#     for  i in range(1,26):
#        message =dechiffrement(cipher , i)
#     return message    
                #######################  cours n°  correction du projet###############
		########################### cours sur les fichiers en  python #############
"""
	1. creer 100 fichiers textes dans le repertoire
       2. ecrire un programme qui supprime le contenu d'un repertoire"
       3. Chiffrer le contenu d'un repertoire
"""
# 1. creation des fichiers textes (fonction) 
import os.path as path
import os 
def create_files( number =1):
          directory_name ="dossier"
          for  i in range(number):
              with open(directory_name+"\\file"+str(i) ,"w"):
                  pass
                       
 
# COURS 4 : Les chaines de caractères en python
import os
def remove_content(directory):
          for dirpath , dirnames , filenames in os.walk(directory, topdown =True):
                    for file in filenames:
                              file_path = os.path.join(directory , file)
                              os.remove(file_path) 
## programme  permettant de chiffrer le contenu d'un repertoire !!!
### fonction permetant de chiffrer le conentu  d'un fichier
               
def file_cipher(file):
          with open(file , mode = "r+") as file:
                    content = file.read()
                    cipher_content = cesar_cipher(content ,cle =4)
                   # new_content = content.replace(content , cipher_content)
                    file.seek(0)
                    file.write(cipher_content ) 
                 
## fonction permettant de chiffrer le contenu d'un repertorie
def dir_cipher(directory):
          for dirpath , dirnames , filenames  in os.walk(directory , topdown = True):
                    for filename  in filenames :
                              file_path = path.join(directory , filename)
                              file_cipher(file_path)           
# ecrire  du text dans l'ensemble des fichier du repertoire dossier
def write_in_file(dossier):
        for  dirpath , dirnames , filenames  in os.walk("./dossier" , topdown = True):
          for file in filenames :
                    file_path = path.join("./dossier" , file)
                    with open(file_path , mode = "w") as fichier:
                              fichier.write("Manipulation des fichiers en  utilisant pyton")

                       
def dir_dechiffrement(directory):
          for dirpath , dirnames , filenames  in os.walk(directory , topdown = True):
                    for filename  in filenames :
                              file_path = path.join(directory , filename)
                              dechiffrement(file_path, cle = 4)
# manipulation des structures de données ?
# introduction à la programmation oriente objet :
class point():
    def __init__(self , x ,y):
        self.__x = x 
        self.__y = y
    def get__x(self):
        return self.__x        
    def get__y(self):
        return self.__y
    def afficher(self):
            print("x :" ,self.get__x() , "y: ", self.get__y())
    def afficher(self , bool =True):
        if bool:
            self.afficher()
        else:
            pass                
        
string = "      ousmane           lo"
print("avant" ,string)
print("apres" , string.split().remove( ""))# p.afficher(False)
                                  
                              
          
                  
                  
           
           
     
            
            
                
              
                
	


			




	
	
	
