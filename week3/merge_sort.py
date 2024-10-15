# Toteuta kurssikirjan luvussa 3.2.1 kuvattu lomitusjärjestäminen Pythonilla.
# Mittaa algoritmin suoritusaika, kun n=105 ja syöte sisältää satunnaisessa 
# järjestyksessä luvut 1,2,…,n.

# Varmista, että algoritmin suorituksen jälkeen syöte on tosiaan järjestyksessä, 
# mutta älä ota tätä mukaan suoritusajan mittaukseen.

# Huom! Algoritmin tulisi olla nopea. Jos algoritmi on hidas, yksi syy voi olla, 
# että et ole käyttänyt globaalia apurakennetta lomituksessa.

import time
import random

def createRandomArray(n):
    arr = []
    for i in range(1,n+1):
        arr.append(i)
    random.shuffle(arr)
    return arr

def isInOrder(t):
    for i in range(len(t)):
        if t[i] != i + 1:
            return False
    return True

def mergeSort(arr):
    if len(arr) > 1: # jos taulukon koko on yksi, on se jo järjestyksessä eli ei tehdä sille mitään
        # jaetaan taulukko kahteen keskikohdasta
        leftArr = arr[:len(arr)//2]
        rightArr = arr[len(arr)//2:]

        # kutsutaan mergeSort rekursiivisesti kummallekin taulukolle
        mergeSort(leftArr)
        mergeSort(rightArr)

        # kun yllä olevat kaksi taulukkoa ovat järjestyksessä, lomitetaan ne yhdeksi suuremmaksi ja järjestetyksi taulukoksi
        # aloitetaan vertailemalla taulukoiden vasemmanpuoleisimpia alkioita
        leftmostA = 0
        leftmostB = 0
        mergedArrIndex = 0

        while leftmostA < len(leftArr) and leftmostB < len(rightArr):
            if leftArr[leftmostA] < rightArr[leftmostB]:
                # vasemman taulukon vasemmanpuoleisin arvo on pienempi,
                # joten tallennetaan se globaaliin arr-taulukkoon
                arr[mergedArrIndex] = leftArr[leftmostA]
                leftmostA += 1
            else:
                # oikeanpuoleisen taulukon vasemmanpuoleisin arvo on pienempi
                arr[mergedArrIndex] = rightArr[leftmostB]
                leftmostB += 1
            mergedArrIndex += 1

        # siirretään loput vasemmanpuoleisesta taulukosta globaaliin taulukkoon
        while leftmostA < len(leftArr):
            arr[mergedArrIndex] = leftArr[leftmostA]
            leftmostA += 1
            mergedArrIndex += 1

        # siirretään loput vasemmanpuoleisesta taulukosta globaaliin taulukkoon
        while leftmostB < len(rightArr):
            arr[mergedArrIndex] = rightArr[leftmostB]
            leftmostB += 1
            mergedArrIndex += 1

if __name__ == "__main__":
    table = createRandomArray(10000)
    print(isInOrder(table))

    start = time.time()
    mergeSort(table)
    end = time.time()
    print("time passed: ", end-start, " s")

    mergeSort(table)
    print(isInOrder(table))