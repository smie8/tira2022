# Toteuta kurssikirjan mukainen dynaamisen ohjelmoinnin algoritmi, 
# joka laskee taulukon pisimmän nousevan alijonon pituuden.

# Testaa algoritmia taulukolla, jossa on satunnaisessa järjestyksessä luvut 1,2,…,n. 
# Minkä tuloksen algoritmi antaa, kun n=5000?

import random

def createRandomArray(n):
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    random.shuffle(arr)
    return arr

def pisin(taulu):
    n = len(taulu)
    pisin = [0] * len(taulu)
    for k in range(n):
        pisin[k] = 1
        for x in range(k):
            if taulu[x] < taulu[k] and pisin[x]+1 > pisin[k]:
                pisin[k] = pisin[x]+1
    pisin.sort()
    return pisin[-1]

if __name__ == "__main__":
    print(pisin([6,2,5,1,7,4,8,3]))
    arr = createRandomArray(5000)
    print(pisin(arr))