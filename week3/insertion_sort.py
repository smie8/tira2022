# Toteuta kurssikirjan luvussa 3.1.1 kuvattu lisäysjärjestäminen Pythonilla. 
# Mittaa algoritmin suoritusaika, kun n=105 ja syöte sisältää satunnaisessa järjestyksessä luvut 1,2,…,n.
import random
import time

def createRandomArray(n):
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    random.shuffle(arr)
    return arr

def insertionSort(t):
    
    start = time.time()

    for i in range(1, len(t)):
        key = t[i]
        j = i-1
        while j >= 0 and key < t[j]:
            t[j+1] = t[j]
            j -= 1
        t[j+1] = key
    
    end = time.time()
    print('time passed: ', end-start, 's')
    
    return t

def isInOrder(t):
    for i in range(len(t)):
        if t[i] != i + 1:
            return False
    return True


if __name__ == "__main__":
    table = createRandomArray(10000)
    print(isInOrder(table))
    insertionSort(table)
    print(isInOrder(table))