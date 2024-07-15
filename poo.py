# introduction à la programmation orienté objet en python
class Citron : 
	saveur = "acide"
	def __init__(this , couleur ):
		this.couleur = couleur
citron = Citron("verte") 
print(citron.couleur  , citron.saveur)	
citron.couleur = "jaune"
citron.saveur = "peu aicde"
print(citron.couleur , citron.saveur)	