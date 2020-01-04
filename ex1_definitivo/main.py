
from btree import BTree


def main():

    a = 2
    b = 6
    tree = BTree(b)

    print("1 esercizio")

    if tree.is_empty():
        print("albero vuoto")

    tree.insert(0, (42,65))

    if not tree.is_empty():
        print("nodo inserito")


if __name__ == '__main__':
    main()