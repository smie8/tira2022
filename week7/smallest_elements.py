# Toteuta testi, jossa syötteenä on n-kokoinen lista lukuja 
# ja halutaan laskea listan n/10 pienimmän alkion summa.

# Toteuta ensin algoritmi 1, joka järjestää listan ja laskee sitten 
# n/10 ensimmäisen luvun summan. Toteuta sitten algoritmi 2, joka 
# lisää ensin luvut kekoon ja hakee sieltä sitten summaan n/10 pienintä lukua.

# Toteuta testi niin, että n=10^6 ja jokainen luku on arvottu 
# satunnaisesti väliltä 1…10^9.

import random
import time
from heapq import heappush, heappop

def algo1(list):
    list.sort()
    sum = 0
    for i in range(len(list)//10):
        sum += list[i]

    return sum

def algo2(list):
    heap = []
    for x in list:
        heappush(heap, x)

    sum = 0
    for i in range(len(list)//10):
        sum += heappop(heap)

    return sum

if __name__ == "__main__":
    list = [random.randint(1, 10**9) for _ in range(10**6)]
    list2 = [random.randint(1, 10**9) for _ in range(10**6)]

    start1 = time.time()
    print(algo1(list))
    end1 = time.time()
    print('algo1 processing time:', end1 - start1, ' s')

    start2 = time.time()
    print(algo2(list2))
    end2 = time.time()
    print('algo2 processing time: ', end2 - start2, ' s')