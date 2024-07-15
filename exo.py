from math import pow
import re 
message = "Bienvenu dans le gestionnaire de Sous-Reseau" 
print(message.lower() ,"\n Que vouliez-vous faire:" )
print("\t1. Calculer une plage d'addresse ip disponible\n" , 
      "\t2. Verifier si une addresse ip appartient à un sous réseau\n",
      "\t3. Convertir une addresse ip en format binaire\n" ,
      "\t4. Convertir une addresse ip en format decimal\n",
      "\t5. quitter\n") 
entree = input()
choice = int(entree)
if entree.isnumeric()== False or int(entree) >5 or int(entree) < 1:
	entree = input("Le choix doit etre [1-5]\t Essayer encore ??:")

#Verifier une bonne adresse et un bon masque de sous reseau
""" une adresse ipv4 est une suite de 4 octets separes par un .
chaque octet doit etre plus petit que 255 
l'adresse est composé de deux partie : une partie hote et une partie reseau defini par le masque"""				
if choice ==1:
	adresse_reseau = input("entrer l'adresse ip\n")
	est_correct_reseau = False 
	while est_correct_reseau == False :
		tab =adresse_reseau.split(".") 
		for element in tab :
			if element.isnumeric() and int(element) < 255 and len(tab) ==4 :
				est_correct_reseau = True
				continue
			else:
				adresse_reseau = input("Adresse invalide : Entrer une autre ??") 
				break
	masque = input("entrer le masque de reseau\n")		
	est_correct_masque = False 
	while est_correct_masque == False :
		tab = masque.split(".") 
		for element in tab :
			if element.isnumeric() and int(element) <= 255 and len(tab) ==4 and int(tab[0]) == 255 :
				est_correct_masque = True
				continue
			else:
				masque = input("Masque  invalide : Entrer un autre ??") 
				break
	# on calcule le nombre de bits  alloué pour la partie reseau ( donc pour la partie hote)
	
	tab = masque.split(".")
	binaire =""
	for index in range(len(tab)):
		binaire_element = ""
		element = int(tab[index])
		for i in range(8):
			binaire_element += str(element%2)
			element = element // 2
		if index !=0:
			binaire_element += "."	
		binaire_element = list(binaire_element)
		binaire_element.reverse()
		binaire += "".join(binaire_element)
	nb_bits_reseau = binaire.count('1')
	
	nb_bits_hote = 32 - nb_bits_reseau
	nb_hotes = int(pow(2, nb_bits_hote)) -2
	"""une fois la partie reseau et la partie hote determiné :  la première adresse de la plage est constitué de la partie reseau à laquelle on replace le rester par des 1
	et pour la derniere adresse de la plage reseau est constituée de la partie réseau à laquelle on remplace le reste par 254
	"""
	chaine = list() # Determinttion de  la première adresse du reseau :::
	for i in range(len(adresse_reseau)):
		if i >= len(adresse_reseau)-masque.count("0")*2 + 1 and  str(adresse_reseau[i]).isnumeric() : ### partie de ce code à verifier encore une fois ::
			chaine.append('1')
			continue
		chaine.append(adresse_reseau[i])
	debut  = "".join(chaine)

	chaine  = list()	#Determination de la dernière adresse du réseau ::	
	for i in range(len(adresse_reseau)):
		if i >= len(adresse_reseau)-masque.count("0")*2+1 and  str(adresse_reseau[i]).isnumeric() :
			chaine.append('254')
			continue
		chaine.append(adresse_reseau[i])
	fin  = "".join(chaine)		
	print("plage d'adresse : " , debut ," - ", fin )
elif choice == 2:
	reseau = input("Entrer le reseau\n")
	est_correct_reseau = False 
	while est_correct_reseau == False : # on recupere l'entre de l'utilisateur tant que l'adresse ip est correcte
		tab =reseau.split(".") 
		for element in tab :
			if element.isnumeric() and int(element) < 255 and len(tab) ==4 :
				est_correct_reseau = True
				continue
			else:
				reseau = input("Adresse invalide : Entrer une autre ??") 
				break
	adresse = input("Entrer l'adresse ip \n")
	est_correct_adresse = False 
	while est_correct_adresse == False : # on continue à demander une adresse tant l'utilisateur n'a donné une bonne adresse ip
		tab =adresse.split(".") 
		for element in tab :
			if element.isnumeric() and int(element) < 255 and len(tab) ==4 :
				est_correct_adresse = True
				continue
			else:
				adresse = input("Adresse invalide : Entrer une autre ??") 
				break
	masque = input("Entrer le masque de reseau\n")	
	est_correct_masque = False
	while est_correct_masque == False :
		tab =masque.split(".") 
		for element in tab :
			if element.isnumeric() and int(element) <=  255 and len(tab) ==4 and int(tab[0]) == 255  :
				est_correct_masque = True
				continue
			else:
				masque = input("Masque invalide : Entrer une autre ??") 
				break
	
	"""Pour verifier q'une adresse ip appartient à un reseau donnée :  
		1. transformer l'adresse ip  et le masque de reseau en question en binaire
		2. Faire une & logique bit à bit entre l'adresse ip et le masque ce qui donne une nouvelle chaine binaire
		3. on transforme e la chaine binaire en decimal en calculant la valeur de chaque octet
	Si la nouvelle adresse obtenu est exactement la meme que l'adress reseau fourni , alors l'adresse ip est bien dans le reseau 
	Sinon l'adresse ip n'y est pas !	

	"""
	#Transformation de l'adresse en  binaire
	net_id = list()	
	
	tab = adresse.split(".") # decoupage de l'adresse en 4 octet et le stocker dans un tableau  et transformer chaque eleement du tableau en binaire
	binaire =""
	for index in range(len(tab)):
		binaire_element = ""
		element = int(tab[index])
		for i in range(8): # on sait d'avance que  l'adresse est composé de 8 bit (1 octet) :::::
			binaire_element += str(element%2)
			element = element // 2
		if index !=0:
			binaire_element += "."	
		binaire_element = list(binaire_element)
		binaire_element.reverse()
		binaire += "".join(binaire_element)
	adress_binaire = binaire.replace(".","")	
	
	tab = masque.split(".")
	binaire =""
	for index in range(len(tab)):
		binaire_element = ""
		element = int(tab[index])
		for i in range(8):
			binaire_element += str(element%2)
			element = element // 2
		if index !=0:
			binaire_element += "."	
		binaire_element = list(binaire_element)
		binaire_element.reverse()
		binaire += "".join(binaire_element)
	masque_binaire = binaire.replace(".","")	
	# on effecture ensuite un & logique entre le masque binaire et l'adresse binaire pour trouver l'adresse du reseau correspondant
	for index in range(32):
		if adress_binaire[index] == masque_binaire[index]:
			net_id.append(adress_binaire[index])
		else:
			net_id.append("0")	
	net_id = "".join(net_id)
	net_id_f = list()
	for index in range(32):
		if index % 8 == 0 and index != 0:
			net_id_f.append(".")
		net_id_f.append(net_id[index])	
	net_id_f = "".join(net_id_f)
	reseau_calculer  = net_id_f
	# on convertie ensuite le reseau binaire trouvé dans les operations precedentes et le comparer au reseau fourni par l'utilisateur
	tab = reseau_calculer.split(".")
	ad =""
	for index in range(4):
		decimal = 0 
		element = list(tab[index])
		element.reverse()
		for i in range(8):
			decimal += int(pow(2,i)) * int(element[i])
		ad += str(decimal)
		if index < 3 :
			ad += "."
	if  ad  == reseau:
		print("L'adresse ip" , adresse , "est bien dans le reseau ", reseau ,"\n")

	else:
		print("L'adresse ip ", adresse ,"n'est pas dans le reseau" , reseau ,"\n")
elif choice == 3:
	adresse = input("Entrer l'adresse ip\n")
	est_correct_adresse = False
	while est_correct_adresse == False :
		tab =adresse.split(".") 
		for element in tab :
			if element.isnumeric() and int(element) < 255 and len(tab) ==4 :
				est_correct_adresse = True
				continue
			else:
				adresse = input("Adresse invalide : Entrer une autre ??") 
				break
	
	# conversion de l'adresse ip en binaire
	tab = adresse.split(".")
	binaire =""
	for index in range(len(tab)):
		binaire_element = ""
		element = int(tab[index])
		for i in range(8):
			binaire_element += str(element%2)
			element = element // 2
		if index !=0:
			binaire_element += "."	
		binaire_element = list(binaire_element)
		binaire_element.reverse()
		binaire += "".join(binaire_element)
	print("adresse ", adresse ,"en binaire : " , binaire)
elif choice == 4:
	adresse = input("Entrer l'adresse ip au format binaire\n")
	est_correct_adresse = False
	while est_correct_adresse == False :
		tab =adresse.split(".") 
		for element in tab :
			if element.isnumeric() and int(element , base = 2) < 255 and len(tab) ==4 :
				est_correct_adresse = True
				continue
			else:
				adresse = input("Adresse invalide : Entrer une autre ??") 
				break
	
	"""
	Pour faire la conversion en decimal , il suffit de chaque bit le multiplier par 2 à la  puissance la postion de ce bit et de faire la somme des resultats obtenu
	"""		
	tab = adresse.split(".")
	ad =""
	for index in range(4):
		decimal = 0 
		element = list(tab[index])
		element.reverse()
		for i in range(8):
			decimal += int(pow(2,i)) * int(element[i])
		ad += str(decimal)
		if index < 3 :
			ad += "."	
	print("l'adresse binaire " ,adresse , "en decimal est : " , ad)

else:
	print("AU REVOIR !!!!")	



	

	