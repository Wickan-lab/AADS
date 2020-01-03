from btree import *
from sortedtablemap import *

def main():
    print("Esercizio 1:")


    """ Sono state utilizzate due liste per l'inserimento degli elementi di un nodo e dei suoi figli. 
        Per la ricerca sono state utilizzate due SortedTableMap per avere una complessità O(logn) 
        IO Complexity dipende dal parametro d = b """



    first = SortedTableMap()
    second = SortedTableMap()



    tree = BTree(6)
    nodo1 = BTree(6)
    nodo2 = BTree(6)
    nodo3 = BTree(6)


    tree.root.elements.insert(0, (42, 65))

    nodo1.root.elements.insert(0, [22, 37])
    tree.root.c.insert(1, nodo1)

    nodo2.root.elements.insert(0, [46, 58])
    tree.root.c.insert(2, nodo2)

    nodo3.root.elements.insert(0, [72, 80, 93])
    tree.root.c.insert(3, nodo3)



    nodo1.root.c.insert(0, [11, 12])


    nodo1.root.c.insert(1, [24,29])
    nodo1.root.c.insert(2, [38,40,41])

    nodo2.root.c.insert(0, [43,45])
    nodo2.root.c.insert(0, [48, 50, 51, 53, 56])
    nodo2.root.c.insert(1, [59, 63])


    nodo3.root.c.insert(0, [66,70])
    nodo3.root.c.insert(1, [74,75])
    nodo3.root.c.insert(2, [83,85,86])
    nodo3.root.c.insert(3, [95,98])


    print(tree)



    #print(tree.firstmap.find_max())

    """tree.insert(42)
    tree.insert(65)

    tree.insert(22)
    tree.insert(37)
    tree.insert(46)
    tree.insert(58)
    tree.insert(72)
    tree.insert(80)
    tree.insert(93)
    tree.insert(11)
    tree.insert(12)
    tree.insert(24)
    tree.insert(29)
    tree.insert(38)
    tree.insert(40)
    tree.insert(41)
    tree.insert(43)
    tree.insert(45)
    tree.insert(48)
    tree.insert(50)
    tree.insert(51)
    tree.insert(56)
    tree.insert(59)
    tree.insert(63)
    tree.insert(66)
    tree.insert(70)
    tree.insert(74)
    tree.insert(75)
    tree.insert(83)
    tree.insert(85)
    tree.insert(86)
    tree.insert(95)
    tree.insert(98)"""


if __name__ == '__main__':
    main()

