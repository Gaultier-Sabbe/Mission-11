#######################################
### TESTS DE LA CLASSE ListeLecture ###
#######################################

from Media import Media
from Duree import Duree
from ListeLecture import ListeLecture

print("TestListeLecture : LAUNCHING TESTS")
print("==================================")

print("TEST 1. Création d'une ListeLecture vide")
print("----------------------------------------")

ll1 = ListeLecture("test", 42)
assert ll1.nombre_de_medias() == 0

print("(test OK)")

print("TEST 2. Affichage d'une ListeLecture vide")
print("----------------------------------------")

print(ll1)
print(ll1.medias)
assert str(ll1.medias) == "[]"

print("(test OK)")

print("TEST 3. Ajouter des médias à une ListeLecture")
print("---------------------------------------------")

ll1.ajouter(Media("test1", "test", Duree(0, 0, 1)))
print(ll1)
print(ll1.medias)
assert ll1.nombre_de_medias() == 1
assert "test1" in str(ll1)

ll1.ajouter(Media("test2", "test", Duree(1, 0, 1)))
print(ll1)
print(ll1.medias)
assert ll1.nombre_de_medias() == 2
assert "test2" in str(ll1)

ll1.ajouter(Media("test3", "test", Duree(0, 1, 1)))
print(ll1)
print(ll1.medias)
assert ll1.nombre_de_medias() == 3
assert "test3" in str(ll1)

ll1.ajouter(Media("test4", "test", Duree(1, 1, 1)))
print(ll1)
assert ll1.nombre_de_medias() == 4
assert "test4" in str(ll1)

print("(test OK)")

print("TEST 4. Affichage d'une ListeLecture non-vide")
print("---------------------------------------------")

print(ll1)
print("(test OK)")

print("TEST 5. Ajouter des médias additionnels à une ListeLecture")
print("----------------------------------------------------------")

#On ajoute encore quelques éléments à ll1
media5 = Media("test5", "test", Duree(0, 0, 2))
ll1.ajouter(media5)
media6 = Media("test6", "test", Duree(0, 59, 59))
ll1.ajouter(media6)
media7 = Media("test7", "test", Duree(0, 0, 3))
ll1.ajouter(media7)
media8 = Media("test8", "test", Duree(0, 0, 59))
ll1.ajouter(media8)
print(ll1)
assert ll1.nombre_de_medias() == 8
assert "test5" in str(ll1)
assert "test6" in str(ll1)
assert "test7" in str(ll1)
assert "test8" in str(ll1)

print("(test OK)")

print("TEST 6. Supprimer des médias d'une ListeLecture")
print("-----------------------------------------------")

print(ll1)
assert ll1.nombre_de_medias() == 8
assert "test1" in str(ll1)
assert "test2" in str(ll1)
assert "test6" in str(ll1)
assert "test7" in str(ll1)
assert "test8" in str(ll1)

ll1.retirer(media6)
assert ll1.nombre_de_medias() == 7
assert "test1" in str(ll1)
assert "test2" in str(ll1)
assert "test6" not in str(ll1)
assert "test7" in str(ll1)
assert "test8" in str(ll1)

ll1.retirer(media8)
assert ll1.nombre_de_medias() == 6
assert "test1" in str(ll1)
assert "test2" in str(ll1)
assert "test6" not in str(ll1)
assert "test7" in str(ll1)
assert "test8" not in str(ll1)
print(ll1)
print("(test OK)")

print("ALL TESTS PASSED")
