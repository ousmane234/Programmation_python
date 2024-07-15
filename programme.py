# def convert_to_bin(ad): # fonction permettant de convertir une adresse ip au format binaire
# 	tab = ad.split(".")
# 	binaire =""
# 	for el in tab:
# 		binaire_element = ""
# 		element = int(el)
# 		for i in range(8):
# 			binaire_element += str(element%2)
# 			element = element // 2
# 		if(tab.index(el) != 0):
# 			binaire_element+="."	
# 		binaire_element = list(binaire_element)
# 		binaire_element.reverse()
# 		binaire += "".join(binaire_element)
# 	return binaire
# print(convert_to_bin("192.168.1.1") ,list(convert_to_bin("192.168.1.1")))
import re
def convert_to_bin(ad): # fonction permettant de convertir une adresse ip au format binaire
	tab = ad.split(".")
	binaire =""
	for index in range(len(tab)):
		binaire_element = ""
		element = int(tab[index])
		for i in range(8):
			binaire_element += str(element%2)
			element = element // 2	
		if index != 0:
			binaire_element =binaire_element+"."		
		binaire_element = list(binaire_element)
		binaire_element.reverse()
		binaire += "".join(binaire_element)
	return binaire
def convert_to_ad (bin): # convertir une adresse au format binaire  en une autre au format decimal
	tab = bin.split(".")
	ad =""
	for index in range(len(tab)):
		decimal = 0 
		element = list(tab[index])
		element.reverse()
		for i in range(8):
			decimal += pow(2,i) * int(element[i])
		ad += str(decimal)
		if index < 3 :
			ad += "."
		
	return ad
print(convert_to_ad("11000000.10101000.00000001.00000000"))	
def trouver_reseau(adresse , masque):
	net_id = list()	
	adress_binaire = convert_to_bin(adresse).replace(".","")
	masque_binaire = convert_to_bin(masque).replace(".","")
	for index in range(32):
		if adress_binaire[index] ==masque_binaire[index]:
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
def replace_last(string , element= ""):
		chaine = list()
		for i in range(len(string)):
			if i == len(string)-1:
				chaine.append(element)
				break
			chaine.append(string[i])
			
		return "".join(chaine)
# sans utiilisation de regex pour trouver une bonne adresse ?
