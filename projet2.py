########################################################           PRESENTATION              ################################
###############  NOM: LO
###############  PRENOM: OUSMANE
###############  NOM DE L'ENSEIGNANT: MOUSSA NDIAYE
###############  COURS: PROGRAMMATION PYTHON
###############  FORMATION : SECURITE DES SYSTEMES EMBARQUES
#################################################################################################################################
						################ CODE SOURCE DU PROJET  ###################
from datetime import datetime 
# Fonction permettant d'afficher une facture (facture forfait internet ou  forfait télé)
# comme l'id du forfait identifie de façon unique un forfait . Il est donc possible d'utiliser une fonction permettant de creer un facture et l'adapter en fonctionn du service  et du forfait
numero_facture = 1 # variable globale contenant le numéro de facture qui doit s'incrementer à chaque facture (appelle de la fontion afficher_facture
nb_abonnes_par_forfait = {"50":0,"150":0 , "500":0 ,"B":0 , "T":0 ,"E":0}
def afficher_facture(id_forfait ,forfait , nom = "" , prenom= "" , numero="" ,adresse="" ):
	# forfait == dictionnaire ( description du forfait   et le prix du forfait ) correspondant à l'id_forfait
	global numero_facture
	global nb_abonnes_par_forfait
	sous_totale = forfait["prix"]
	tva = (sous_totale * 18)//100 # egal à 18% du sous totale
	montant_total= sous_totale + tva 
	print("\n")
	print("\t"*4 ," ## facture ##")
	print("____________________________________________________________________________________")## information sur sengalConnect::
	print("Senegal-connect\n UCAD - LACGAA - MS2E 2024\n Facture n° : " ,numero_facture , "\t \t " , datetime.now().date() ,"  " , datetime.now().time().strftime("%H:%M:%S"))
					## information sur le client :::
	print("_____________________________________________________________________________________")
	print("Prenom et nom du client : " , prenom ," " ,nom ,"\t  numéro de téléphone: ", numero)
	print("Adresse du client : " ,adresse)
	print("\n")
	print("Description - forfait                                                         prix")
	print("-".ljust(85,"-"))
	print(forfait["description"].ljust(70 ," "),forfait["prix"],"CFA")
	print("Sous totale ".ljust(70, " "),sous_totale ,"CFA")
	print("Montant TVA ".ljust(70, " "),tva,"CFA")
	print("Montant totale ".ljust(70, " "),montant_total,"CFA")
	print("-".ljust(85 , "-"))
	print("Merci de  votre confiance\n".ljust(40, " "))
	numero_facture += 1
	nb_abonnes_par_forfait[id_forfait] += 1
					
print (" -------------------------------------------------------------------") 
print("|Bienvenu dans le systeme de facturation  d'Internet-Télé pour Tous.".ljust(60 , " "),"|\n"
      "|Ce system permet de calculer la facture des  abonnés selon le prix ".ljust(60 , " "),"|\n"
      "|et le nombre de forfaite choici. Il affiche aussi le nombre ".ljust(70 ," "),"|\n"
      "|d'abonnés par forfait ".ljust(70 ," "), "|")
print(" ---------------------------------------------------------------------")
print("\t *** Menu de choix ***\n" ,
      "\t1. Facturer un Abonnement\n" ,
      "\t2. Afficher le nombre d'abonnés par forfait\n" , 
      "\t3. Quitter le programme")
while True:
	option = int(input("Entrer votre option:"))
	# nb_abonnes ={"50": 0 ,"150":0, "500":0 ,"B":0 ,"T":0 ,"E":0}
	services = (1,2 ,3) # Les services possibles
	## Chaque forfait (internet  ou tele) possede un id , une description , et un prix : il est donc judicieux d'utiliser un dictionnaire
	## de sorte que  connaissant l'id , on puisse acceder à la description et le prix du forfait
	forfaits_internet = { # les forfaits internets  : description et prix de chaque forfait
		"50":{"description": "Internet fibre hybride 50" ,"prix": 12500} ,
		"150":{"description":"internet fibre hybride 150" , "prix":15250 } ,
		"500":{"description": "internet fibre hybride 500" , "prix": 20500}
	}
	forfaits_tele = { # forfaits tele : description et prix de chaque forfait !
		"B":{"description":"Forfait Bien -choix 15 chaines à la carte" , "prix": 4900},
		"T":{"description":"Forfait Tres Bien - choix de 25 chaines à la carte", "prix": 8400},
		"E":{"description" : "Forfait excellent - choix de 35 chaines à la carte" , "prix": 12500}
	}
	if option ==1: # achat d'un forfait
		nom = input("Entrer le nom de l'abonné:   ") 
		prenom = input("Entrer le prenom de l'abonné:  ")
		numero = input("Entrer le numéro de l'abonné:  ")
		adresse = input("Entrer l'adresse de l'abonné:  ")
		
		while True :
			service = int(input("Entrer les numéro des services \n(1 = Internet , 2 = Télé , 3 = Internet et Télé) :" ) )
			if service not in services:
				print( "numéro de service inconnu") 
				continue # redemander des numéros de  services
			else :
				break  # sinon :  on continue les traitement
		if service == 1 : # l'utilisateur veut un forfati  internet !!
			while True :
				id_forfait = input("Entrer l'identifiant du forfait (50 , 150 ,500) : "  )
				if id_forfait not in forfaits_internet.keys():
					print("numéro de forfait invalide :\n")
					continue
				else:
					forfait =forfaits_internet[id_forfait]
					# sous_totale = forfait["prix"]
					# si l'utilisateur  ajout un forfait un internet ,on doit increment le nombre d'abonne de ce forait là
					# pour pouvoir ensuit l'utiler dans le traitement de la partie2.
					# nb_abonnes[forfait] += 1 
					afficher_facture( id_forfait , forfait , nom=nom , prenom = prenom, adresse = adresse , numero = numero  )
					break
				
		elif service == 2: # l'utilisateur veut un forfait tele !!
			while True:
				id_forfait = input("Entrer  l'identifiant du forfait \n\t>> B = Forfait bien -choix de 15 chaine à la carte ,\n\t>> T = Forfait Trés Bine -choix de 25 chaine à la carte\n\t>> E = Excellent -choix de 35 chaine à la carte)  : ")
				if id_forfait not in forfaits_tele.keys():
					print("Le numero  forfait est invalide\n")
					continue
				else: 
					forfait = forfaits_tele[id_forfait]
					# sous_totale =  forfait["prix"]
					# nb_abonnes[forfait] += 1 # increment  le nombre d'abonnés de ce forfait à 1
					afficher_facture(id_forfait  , forfait,nom= nom  ,prenom = prenom , adresse= adresse , numero= numero)
					break	
		else: # service 3 ( internet +  tele)
			while True :
				id_forfait_internet = input("Entrer l'identifiant du  forfait innternet  (50 ,150 ,500) : ")
				id_forfait_tele = input("Entrer  l'identifiant du forait  tele (B ,T , E) : ")
				if id_forfait_internet not in forfaits_internet.keys() or id_forfait_tele not in forfaits_tele.keys():
					print("numéro du forfait internet ou télé invalide \n")
					continue 
				else:
					print("\n")
					print("_____________________________________________________________________________________")
					print("Prenom et nom du client : " , prenom ," " ,nom ,"\t  numéro de téléphone: ", numero)
					print("Adresse du client : "                                                      ,adresse)
					print("\n")
					print("Description - forfait                                                         prix")
					print("-----------------------------------------------------------------------------------")
					print(forfaits_internet[id_forfait_internet]["description"].ljust(70 ," ") , forfaits_internet[id_forfait_internet]["prix"] ," CFA")
					print(forfaits_tele[id_forfait_tele]["description"].ljust(70 ," ") ,forfaits_tele[id_forfait_tele]["prix"], " CFA")
					print("------------------------------------------------------------------------------------")
					print("\t"*4 ,"Merci de  votre confiance\n")
					nb_abonnes_par_forfait[id_forfait_internet]   += 1
					nb_abonnes_par_forfait[id_forfait_tele] += 1
					break ;		# faire les traitements correspondants sur les forfaits tele et internet ?		
	elif option == 2: # consulter le nombre d'abonnés de chaque forfaits !
		print("-----------------------------------------------------------------------")
		print("Senegal Connect")
		print("Date et Heure:\t" , datetime.now().date(), "  " , datetime.now().time().strftime("%H:%M:%S"))
		print("------------------------------------------------------------------------")
		print("Forfaits Nb. d'abonnés")
		print("********************************************************************")
		print("Internet fibre hybride 50                                       :", nb_abonnes_par_forfait["50"])
		print("Internet ifbre hybride 150                                      :", nb_abonnes_par_forfait["150"])
		print("Internet fibre hybride 500                                      :", nb_abonnes_par_forfait["500"]) 
		print("Forfait bien - choix de 15 chaines à la carte                   :", nb_abonnes_par_forfait["B"])
		print("Forfait très bien - choix de 25 chaines à la carte              :", nb_abonnes_par_forfait["T"])
		print("Forfait Excellent - choix de 35 chaines à la carte       	:", nb_abonnes_par_forfait["E"])
		print("---------------------------------------------------------------------")
		
	else: # quitter le programme !
		print("Au revoir !!!")
		break 




	
