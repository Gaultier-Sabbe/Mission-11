################################
### TESTS DE LA CLASSE Media ###
################################

from Duree import Duree
from Media import Media

print("TestMedia : LAUNCHING TESTS")

print("TEST 1. Création de trois objets de type Media")
chanson1 = Media("test1", "test", Duree(0, 1, 30))
chanson2 = Media("test2", "test", Duree(1, 1, 30))
chanson3 = Media("test3", "test", Duree(0, 1, 31))
print("(test OK)")

print("TEST 2. Taille des objets de type Media")
assert chanson1.taille() == 0.05*chanson1.duree.to_secondes()
assert chanson2.taille() == 0.05*chanson2.duree.to_secondes()
assert chanson3.taille() == 0.05*chanson3.duree.to_secondes()
print("(test OK)")

print("TEST 3. Affichage des objets de type Media")
print(chanson1)
assert str(chanson1) == "(00:01:30, 4.5MB) 'test1' par test"
print(chanson2)
assert str(chanson2) == "(01:01:30, 184.5MB) 'test2' par test"
print(chanson3)
assert str(chanson3) == "(00:01:31, 4.55MB) 'test3' par test"
print("(test OK)")

# A AJOUTER PAR LES ETUDIANTS
print("TEST 4. Egalité des objets de type Media")
chanson1bis = Media("test1", "test", Duree(1, 1, 30))
# chanson avec le même nom et artiste que chanson 1, sera considéré comme égale à chanson1
assert chanson1 == chanson1bis
assert not ( chanson1 is chanson1bis )
assert not ( chanson1 == chanson3 )
assert not ( chanson1 is chanson3 )
assert not ( chanson2 == chanson3 )
assert not ( chanson2 is chanson3 )
print("(test OK)")

print("TEST 5. Comparaison des objets de type Media")
assert chanson1 < chanson2
assert chanson2 > chanson1
assert not chanson3 < chanson2
print("(test OK)")

print("ALL TESTS PASSED")