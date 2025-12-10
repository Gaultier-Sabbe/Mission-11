from OrderedLinkedList import OrderedLinkedList

def to_py_list(oll):
    """
    Convertit une OrderedLinkedList en liste Python [v1, v2, ...]
    en parcourant les Node via first() et next().
    """
    values = []
    current = oll.first()
    while current is not None:
        values.append(current.value())
        current = current.next()
    return values

# Tests du constructeur

def test_init_vide():
    lst = OrderedLinkedList()
    assert lst.size() == 0
    assert lst.first() is None
    assert lst.last is None
    print("Test réussi :\ttest_init_vide()")


def test_init_avec_liste_non_triee():
    lst = OrderedLinkedList([3, 1, 4, 2])
    assert lst.size() == 4
    assert to_py_list(lst) == [1, 2, 3, 4]
    assert lst.first().value() == 1
    assert lst.last.value() == 4
    print("Test réussi :\ttest_init_avec_liste_non_triee()")


# Tests de add()

def test_add_sur_liste_vide():
    lst = OrderedLinkedList()
    lst.add(5)
    assert lst.size() == 1
    assert to_py_list(lst) == [5]
    assert lst.first().value() == 5
    assert lst.last.value() == 5
    print("Test réussi :\ttest_add_sur_liste_vide()")


def test_add_insertion_en_tete():
    lst = OrderedLinkedList()
    lst.add(10)
    lst.add(7)
    lst.add(3)
    assert lst.size() == 3
    assert to_py_list(lst) == [3, 7, 10]
    assert lst.first().value() == 3
    assert lst.last.value() == 10
    print("Test réussi :\ttest_add_insertion_en_tete()")


def test_add_insertion_au_milieu():
    lst = OrderedLinkedList()
    lst.add(1)
    lst.add(5)
    lst.add(10)
    lst.add(7)
    assert lst.size() == 4
    assert to_py_list(lst) == [1, 5, 7, 10]
    print("Test réussi :\ttest_add_insertion_au_milieu()")


def test_add_insertion_a_la_fin():
    lst = OrderedLinkedList()
    lst.add(1)
    lst.add(2)
    lst.add(3)
    lst.add(10)
    assert lst.size() == 4
    assert to_py_list(lst) == [1, 2, 3, 10]
    assert lst.last.value() == 10
    print("Test réussi :\ttest_init_vide()")


def test_add_avec_doublons():
    lst = OrderedLinkedList()
    lst.add(5)
    lst.add(3)
    print("Test réussi :\ttest_add_avec_doublons()")
    

# Appelle de tous les tests

test_init_vide()
test_init_avec_liste_non_triee()
test_add_sur_liste_vide()
test_add_insertion_en_tete()
test_add_insertion_au_milieu()
test_add_insertion_a_la_fin()
test_add_avec_doublons()