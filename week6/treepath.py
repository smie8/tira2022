from collections import namedtuple

# (vastaus eli reittien pituuksien summa, reitin pituus)
def calc(node):
    # if not node:
    #     return 1
    # left = calc(node[0])
    # right = calc(node[1])

    # answer = left+right
    # return answer
    if not node:
        return (1, 1)
    # haetaan vastaukset alipuista:
    left = calc(node[0])
    right = calc(node[1])

    answer = left[0]+right[0] + 1
    lengths = left[1] + right[1]
    print(answer,lengths)

    return (answer, lengths)

def count2(node):
    return calc(node)[0]

def count(node):
    if not node:
        return 0
    return count(node[0])+count(node[0])+1

# def count(node):
#     if not node:
#         return 0
#     if not node[0] and not node[1]:
#         return 1

#     return count(node[0]) + count(node[1])

if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(Node(None,None),Node(Node(None,None),Node(None,None)))
    print(count(tree)) # 8