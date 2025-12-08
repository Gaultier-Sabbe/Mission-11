############################################
### TESTS DE LA CLASSE LinkedList ###
############################################

from LinkedList import LinkedList

print("TestLinkedList : LAUNCHING TESTS")

print("TEST 1. Création d'une LinkedList vide")
ll = LinkedList()
print(ll)
assert ll.size() == 0
print("(test OK)")

print("TEST 2. Ajouter des éléments à une LinkedList")
# créer une liste contenant les valeurs 'a', 'b', 'c', 'd', 'e,' 'f' dans cet ordre
# (pour obtenir cet ordre on doit les ajouter dans l'ordre opposé, car les nouveaux
# éléments sont toujours ajoutés au début de la liste châinée)
assert ll.size() == 0
ll.add("f")
print(ll)
assert ll.size() == 1
ll.add("e")
print(ll)
assert ll.size() == 2
ll.add("d")
print(ll)
assert ll.size() == 3
ll.add("c")
print(ll)
assert ll.size() == 4
ll.add("b")
print(ll)
assert ll.size() == 5
ll.add("a")
print(ll)
assert ll.size() == 6
print("(test OK)")

print("TEST 3. Après la création d'une LinkedList les éléments se trouvent dans le bon ordre")
# c'est-à-dire le dernier ajouté au début de la liste et le premier ajouté à la fin de la liste
print(ll)
assert str(ll) == "[ a b c d e f ]"
print("(test OK)")

print("TEST 4. On ajoute encore quelques éléments à la liste et on vérifie l'ordre")
ll.add("b")
assert ll.size() == 7
print(ll)
ll.add("d")
assert ll.size() == 8
print(ll)
ll.add("a")
assert ll.size() == 9
print(ll)
assert str(ll) == "[ a d b a b c d e f ]"
print("(test OK)")

print("TEST 5. La suppression d'un élément d'une LinkedList fonctionne correctement")
assert ll.size() == 9
assert str(ll) == "[ a d b a b c d e f ]"
print(ll)
ll.remove()
assert ll.size() == 8
assert str(ll) == "[ d b a b c d e f ]"
print(ll)
ll.remove()
assert ll.size() == 7
assert str(ll) == "[ b a b c d e f ]"
print(ll)
ll.remove()
assert ll.size() == 6
assert str(ll) == "[ a b c d e f ]"
print(ll)
ll.remove()
assert ll.size() == 5
assert str(ll) == "[ b c d e f ]"
print(ll)
ll.remove()
assert ll.size() == 4
assert str(ll) == "[ c d e f ]"
print(ll)
ll.remove()
assert ll.size() == 3
assert str(ll) == "[ d e f ]"
print(ll)
ll.remove()
assert ll.size() == 2
assert str(ll) == "[ e f ]"
print(ll)
ll.remove()
assert ll.size() == 1
assert str(ll) == "[ f ]"
print(ll)
ll.remove()
assert ll.size() == 0
assert str(ll) == "[ ]"
print(ll)
print("(test OK)")

print("ALL TESTS PASSED")
