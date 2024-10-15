# Minimikeko sisältää luvut 1…n. 
# Kuinka monessa eri kohdassa luku k voi sijaita? 
# Voit olettaa, että n on korkeintaan 100 ja että 1≤k≤n.

from heapq import heappush, heappop
import math

def count2(n, k):
    height = math.ceil(math.log2(n + 1))
    numsInLevel = 1
    level = 1
    print(numsInLevel)

    while level <= height:
        numsInLevel *= 2
        print(numsInLevel)
        level += 1

    # math.floor(math.log2(num))
    print('---')

    return height

def count(n, k):
    numsInLastRow = 0
    height = math.ceil(math.log2(n + 1))
    numsLeft = n
    positions = 0

    level = 1
    numsInLevel = 1
    num = 1

    if k == 1:
        return 1

    while numsLeft > 0:
        if level == height:
            possibleEmptyPositionsInLastRow = 0
            # edellisen rivin lapsettomat solmut ovat myös mahdollisia positioita:
            if height > 2:
                possibleEmptyPositionsInLastRow = numsInLevel // 2 - (numsLeft//2)

            positions = numsLeft + possibleEmptyPositionsInLastRow
        else:
            numsInLastRow = numsInLevel


        numsLeft -= numsInLevel

        numsInLevel *= 2
        num += numsInLevel
        level += 1

    return positions

if __name__ == "__main__":
    print(count(2,2)) # 1
    print(count(4,2)) # 2
    print(count(1,1)) # 1
    print(count(3,2)) # 2
    print(count(5,4)) # 3
    print(count(5,5)) # 3
    print(count(10,9)) # 6
    print(count(70,34)) # 68