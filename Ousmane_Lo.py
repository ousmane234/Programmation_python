### programme permettant la gestion des employes
### 1. Ajouter un employe
id = 1
print(" 1. ajouter  un employe \n 2. Supprimer une employe \n 3. Rechercher un employe \ 4.Afficher la liste complete des employes \n 5.Afficher le salaire moyen d'un employe " )
option = int(input ("ajouter  une option :\n"))
# 1. ajouter un employe:
import os
def ajouterEmploye():
          nom = input("Entrer le nom de l'employe")
          prenom = input("Entrer le prenom de l'employe")
          nationalite = input("Entrer la nationalite de l'employe")
          salaire = input("Entrer le salaire de l'employe")
          with open("employe.txt"  ,mode = 'a') as file:
                    file.write(id , " " ,nom ," " , prenom ," " , nationalite , " " , salaire, " " )
                    id +=1
def supprimerEmploye():
          identifiant = int(input("Entrer l'identifiant de l'employe"))
          employes =[]
          with open("employe.txt" ,mode ='r') as file:
                    employes = file.readlines()
                    for line in employes:
                              if identifiant in line:
                                        employes.remove(line)
          with open("employe.txt" , mode ='w')as file:
                    file.writelines(employes)
def rechercherEmploye():
          identifiant = int(input("Entrer l'identifiant de l'employe"))
          with open("employe.txt" ,mode ='r') as file:
                    employes = file.readlines()
                    for line in employes:
                              if identifiant in line:
                                        print(line)
                                        break
                              
                              
def afficherEmploye():
          with open("employe.txt", mode ='r') as file:
                    for line in file.readlines():
                              print(line)
                               
                              
def salaire_moyen():
          salaires=[]
          with open("employe.txt", mode ='r') as file:
                   for line in file.readlines:
                             salaires.append(line.spit(" ")[4])
          return  sum(salaires)/(len(salaires))
          
def mieux_payes():
          moyenne = salaire_moyen()
          with open("employe.txt" , mode ='r') as file:
                    for line in file.readlines():  
                              if(line.split(" ")[4]>moyenne):
                              	print(line)




if option ==1 :
          ajouterEmploye()
elif option ==2:
          supprimerEmploye()
elif option ==3 :
          rechercherEmploye()
elif option ==4:
          afficherEmploye()
elif option ==5:
	print(salaire_moyen())
elif option ==6:
          mieux_payes()

                    
           
                                        
                              
                    
          