class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
def arrToBst(arr):
    if not arr:
        return None
 
    middleIndex = len(arr) // 2

    rootNode = Node(arr[middleIndex])
    rootNode.left = arrToBst(arr[:middleIndex])
    rootNode.right = arrToBst(arr[middleIndex + 1:])

    return rootNode

def preOrder(node, returnArr):
    if not node:
        return
    
    returnArr.append(node.value)
    # print(node.value)
    preOrder(node.left, returnArr)
    preOrder(node.right, returnArr)

def create(n):
    arr = list(range(1, n+1))
    arr.sort()
    rootNode = arrToBst(arr)
    returnArr = []
    preOrder(rootNode, returnArr)
    return returnArr

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2, 3, 1]
    print(create(4)) # [2, 1, 4, 3]
    print(create(7)) # [4, 6, 5, 2, 3, 7, 1]