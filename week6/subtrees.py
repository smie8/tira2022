# Tehtäväsi on laskea suurin ero vasemman ja oikean alipuun solmujen määrässä 
# jossain binääripuun solmussa. Voit olettaa, että puussa on enintään 100 solmua

from collections import namedtuple

def count(node, ans):
    if not node:
        return (0, 0)

    left = count(node.left, ans)
    right = count(node.right, ans)

    diff = abs(left[1] - right[1])

    ans[0] = max(diff, ans[0])

    size = left[1] + right[1] + 1

    return (diff, size)

def diff(node):
    ans = [0]
    count(node, ans)
    return ans[0]

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])

    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(diff(tree)) # 3

    tree2 = Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=None))
    print(diff(tree2)) # 4