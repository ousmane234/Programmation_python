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
choice = 0
if entree.isnumeric()== False or int(entree) >5 or int(entree) < 1:
	entree = input("Le choix doit etre [1-5]\t Essayer encore ??:")
choice = int(entree)
#Verifier une bonne adresse et un bon masque de sous reseau
""" une adresse ipv4 est une suite de 4 octets separes par un .
chaque octet doit etre plus petit que 255 
l'adresse est composé de deux partie : une partie hote et une partie reseau defini par le masque"""			
regex_adresse = re.compile(r"((25[0-5]?|2[0-4]?[0-9]?|[5-9]\d?|[01]\d{,3})\.){3}(25[0-5]?|2[0-4]?[0-9]?|[01]\d{,3})$")
regex_masque = re.compile(r"(255\.){1,3}(25[0-4]\.|2[0-4]?\d\.|[01]?\d{,2}\.){,2}(25[0-4]|2[0-4]?\d?|[1]?\d{,2}|)?$")
def convert_to_bin(ad): # fonction permettant de convertir une adresse ip au format binaire
	tab = ad.split(".")
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
	return binaire
def convert_to_ad (binaire): # fonction permettant de convertir une adresse ip du binaire au format decimal
	tab = binaire.split(".")
	ad =""
	for index in range(4):
		decimal = 0 
		element = list(tab[index])
		element.reverse()
		for i in range(8):
			decimal += int(pow(2,i)) * int(element[i]) # conversion de la fonction pow qui retourne un double
		ad += str(decimal)
		if index < 3 :
			ad += "."	
	return ad		
## fonction permettant de trouver le reseau en fonction de l'adresse et du masque
def trouver_reseau(adresse , masque):
	net_id = list()	
	adress_binaire = convert_to_bin(adresse).replace(".","")
	masque_binaire = convert_to_bin(masque).replace(".","")
	for index in range(32):
		if adress_binaire[index] == masque_binaire[index]:
			net_id.append(adress_binaire[index])
		else:
			net_id.append("0")	
	net_id = "".join(net_id)
	# Decoupons notre net id en bloc d'octets (8 bits) séparés par des "."
	net_id_f = list()
	for index in range(32):
		if index % 8 == 0 and index != 0:
			net_id_f.append(".")
		net_id_f.append(net_id[index])	
	net_id_f = "".join(net_id_f)
	return net_id_f
def replace_last(string , element= "", count = 1):
		chaine = list()
		for i in range(len(string)):
			if i >= len(string)-count and  str(string[i]).isnumeric() :
				chaine.append(element)
				continue
			chaine.append(string[i])
			
		return "".join(chaine)		
############## fin de declaration de fonctions ##########################################""		
if choice ==1:
	adresse_reseau = input("entrer l'adresse ip\n")
	masque = input("entrer le masque de reseau\n")
	while not  regex_adresse.fullmatch(adresse_reseau):
		adresse = input("Adresse non valide \tReessayer??\n")
	while not regex_masque.fullmatch(masque):
		masque = input("Masque de sous reseau invalide\tReessayer??\n")
	# on calcule le nombre de bits  alloué pour la partie reseau ( donc pour la partie hote)
	nb_bits_reseau = convert_to_bin(masque).count('1')
	nb_bits_hote = 32 - nb_bits_reseau
	nb_hotes = int(pow(2, nb_bits_hote)) -2
	debut = replace_last(adresse_reseau ,"1" , masque.count("0"))
	fin = replace_last(adresse_reseau ,"254" , masque.count("0"))
	print("plage d'adresse : " , debut ," - ", fin )
	# on cherche maintenant les plages d'adresses pour le reseau
elif choice == 2:
	reseau = input("Entrer le reseau\n")
	masque = input("Entrer le masque de reseau\n")
	adresse = input("Entrer l'adresse ip \n")
	######## on verifie si les entres sont bonnes ou pas 
	while not regex_adresse.fullmatch(reseau):
		reseau = input("Adresse reseau non valide \t ,Reesayer??\n")
	while not regex_adresse.fullmatch(adresse):
		adresse = input("Adresse ip non valide \t Reessayer??\n")
	while not regex_adresse.fullmatch(masque):
		masque = input("Masque de reseau non valide \t Reessayer??\n")
	reseau_calculer = trouver_reseau(adresse,masque)
	if re.fullmatch (convert_to_ad(reseau_calculer) , reseau):
		print("L'adresse ip" , adresse , "est bien dans le reseau ", reseau ,"\n")

	else:
		print("L'adresse ip ", adresse ,"n'est pas dans le reseau" , reseau ,"\n")
elif choice == 3:
	adresse = input("Entrer l'adresse ip\n")
	while not regex_adresse.fullmatch(adresse):
		adresse = input("Adresse non valide \t Reessayer??")
	print(adresse ,"en binaire est : " , convert_to_bin(adresse))	
elif choice == 4:
	adresse = input("Entrer l'adresse ip au format binaire\n")
	while not regex_adresse.fullmatch(adresse):
		adresse = input("Adresse ip non valide \t Reessayer??")
	print(adresse ," au format decimal est : ", convert_to_ad(adresse))	
else:
	print("AU REVOIR !!!!")	



	

	