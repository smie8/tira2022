# Tehtäväsi on laskea, montako solmua on annetussa binääripuussa tietyllä tasolla. 
# Puun juuri on tasolla 1, sen lapset ovat tasolla 2, jne. 
# Voit olettaa, että puussa on enintään 100 solmua.

from collections import namedtuple

def count(node, level, currentLevel=1):
    if node == None:
        return 0
    if currentLevel == level:
        return 1
    return count(node.left, level, currentLevel + 1) + count(node.right, level, currentLevel + 1)

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree,1)) # 1
    print(count(tree,2)) # 1
    print(count(tree,3)) # 2
    print(count(tree,4)) # 0