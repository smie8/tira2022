# Toteuta testi, jossa syötteenä on n-kokoinen lista lukuja ja halutaan laskea, 
# montako eri lukua listalla on.

# Toteuta ensin algoritmi 1, joka järjestää listan luvut ja laskee eri lukujen 
# määrän tutkimalla vierekkäisiä lukuja. Toteuta sitten algoritmi 2, joka laskee 
# eri lukujen määrän laittamalla luvut hajautustauluun.

# Toteuta testi niin, että n=10^6 ja jokainen luku on arvottu satunnaisesti väliltä 1…10^9.


import random
import time

def createRandomArray(n):
    arr = []
    for i in range(1,n+1):
        arr.append(random.randint(1, 1000000000))
    return arr

def differentNumbers(arr):
    arr.sort()
    count = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            count += 1

    return count

def differentNumbersHashTable(arr):
    hashTable = set()

    for x in arr:
        hashTable.add(x)

    return len(hashTable)

arr = createRandomArray(1000000)
startTime1 = time.time()
print(differentNumbers(arr))
endTime1 = time.time()
print('time passed:', endTime1 - startTime1, ' s')

startTime2 = time.time()
print(differentNumbersHashTable(arr))
endTime2 = time.time()
print('time passed:', endTime2 - startTime2, ' s')
