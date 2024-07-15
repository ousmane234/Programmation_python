# introductionn au expressions regulières et parsing en python
"""une expression regulière est une suite de caractère qui a pour but de decrire un fragment de text
ou motif ( pattern en anglais)"""
# le module re : pour tout ce qui est expression regulière en python
import re 
import os
chaine = "Bonjour le monde depuis mon fichier Regex" 
if re.search("mon",chaine): # la fonction search  : chercher un motif dans une chaine de caract
	print("sous chaine trouvé ")
if re.match("Bon", chaine): # fonction match : comme search mais seulement si  la regex correspond au debut de la chaine de carac
	print("Oui debut de la chaine")	
if re.fullmatch("Bonjour le monde depuis mon fichier Regex", chaine): # fonction fullmatch  : comme match mais @ seulement si la regex corresponde exactement à la chaine
	print("correspondance totale")	

regex = re.compile("(\d+)\.(\d+)") # Creer un objet regex
print(type(regex))
resultat = regex.search("Pi vaut 3.14 et pi vaut 2.72") # retourne la premiere expressio trouvé
print(type(resultat))
debut = resultat.start() # retourner l'index de debut de la  sous chaine(regex)
fin = resultat.end() # l'indice de fin de la sous chaine (regex)
print(debut , fin)
tout = regex.findall("pi vaut 3.14 et e vaut 2.72")# methode findall() recherche toutes les expressions correspond et retourn un tableau
print(tout)
new_string = regex.sub("?" , "pi vaut 3.14 et  e vaut 2.72") # method sub(chaine1, chaine2) remplace toutes occurence de l'exp dans chaine2 par chaine1
print(new_string)
# programme permettant de remplacer les espace mutiple dans un  text par un seul espace
espace = re.compile("\s+") # \s designe un espace 
with open("fich.txt",mode = "r" , encoding = "UTF 8") as file  , open("fichier.txt",mode = "w" ,encoding = "UTF 8") as file2:
	for line in file.readlines():
		line = espace.sub(" ", line)
		file2.write(line+"\n")
regex_masque = re.compile(r"(\d{1,3}\.){3}\d{1,3}$")
print(regex_masque.fullmatch("255.255.255.29"))	
