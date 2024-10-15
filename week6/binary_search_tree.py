# Toteuta kurssikirjan luvun 6.2 mukainen binäärihakupuu, jossa pystyy 
# lisäämään alkion puuhun sekä laskemaan puun korkeuden.

# Jos puuhun lisättäisiin alkiot 1,2,…,n pienimmästä suurimpaan, puun 
# korkeudeksi tulisi n−1. Entä jos alkiot lisätäänkin satunnaisessa järjestyksessä?

# Toteuta testi, jossa n=10^5 ja alkiot 1,2,…,n lisätään satunnaisessa järjestyksessä. 
# Mikä on puun korkeus kaikkien lisäysten jälkeen?

# Voit tallentaa jokaisen solmun Node-luokan oliona, jossa on viittaus vasempaan 
# ja oikeaan lapseen sekä solmussa oleva arvo. 
# Seuraavassa on esimerkki, miten luokan voi tehdä Pythonilla.
# class Node:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value


# lisää alkio puuhun
# laske korkeus

import random

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def createRandomArray(n):
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    random.shuffle(arr)
    return arr

def createTree(arr):
    bst = []
    root = Node(arr[0])
    bst.append(root)

    for i in range(1, len(arr)):
        value = arr[i]
        for x in bst:
            insert(x, value, height)

    print('height', height)
    return bst

def insert(node, value, height):
    if value < node.value:
        if node.left is not None:
            insert(node.left, value, height)
        else:
            node.left = Node(value)
    else:
        if node.right is not None:
            insert(node.right, value, height)
        else:
            node.right = Node(value)

def height(root):
    if root is None:
        return 0

    leftHeight = height(root.left)
    rightHeight = height(root.right)

    return max(leftHeight, rightHeight) + 1

if __name__ == "__main__":
    arr = createRandomArray(10**5)
    print(arr)
    bst = createTree(arr)

    print(height(bst[0]))