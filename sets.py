#manipulation des sets et frozensets
"""
1. les sets ne peuvent pas contenir de doublons : les doublons sont implicitement effacés
2.les sets sont non indexables
3. les set ne peuvent etre modifié que par des fonctions spécifiques
"""
liste = [2,3,9,9,8] 
new_set = set(liste)
print(new_set)
s ={1,3,5,4,5}
s.add(9) # ajouter l'element 9
s.update(list(liste)) # faire la reunion de s et de liste sans doublons
s.remove(9) # supprimer l'element 9
s.difference(new_set) # retourne une nouvelle set contenu la difference entre s et new_set
s.pop() # supprime le premier element de la structure
s.intersection(new_set) # retourne une nouvelle set contenant l'inetersection entre s et new__set
#s.clear()#vider le contenu de s
print(s)
sequence = "Bonjour le monde depuis mon fichier sets.py .. Je veux compter la frequence d'apparition de chaque lettre dans la phrase"

ma_set = set(sequence)
print([(element , sequence.count(element)) for element in ma_set])



