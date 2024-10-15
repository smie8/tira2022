# Annettuna on lista lukuja ja tehtäväsi on selvittää, montako lukua listalta 
# voidaan valita siten, että minkään kahden valitun luvun erotus ei ole suurempi kuin x.

# Voit olettaa, että listalla on enintään 105 lukua ja x ja jokainen listan luku 
# on väliltä 0…109. Tavoitteena on, että algoritmin aikavaativuus on O(n) tai O(nlogn).

# Toteuta tiedostoon bigset.py funktio find, joka ilmoittaa montako lukua 
# listalta voidaan enintään valita.

def find(t, x):
    t.sort()

    biggestSet = 1
    smallest = t[0]
    smallestIndex = 0
    count = 1

    for i in range(1, len(t)):
        # käy järjestetty lista läpi
        # kirjaa ylös pienin luku ja sen indeksi

        if t[i] - smallest <= x:
            count += 1
        else:
            smallestIndex += 1
            smallest = t[smallestIndex]

        if count > biggestSet:
            biggestSet = count

    return biggestSet

if __name__ == "__main__":
    print(find([13, 5, 14, 5, 13], 4), 3) # 3

    print(find([2, 7, 14, 11, 7, 15], 11), 5) # 5
    print(find([10, 10, 10, 10], 0),4) # 4
    print(find([4, 2, 7, 1], 0), 1) # 1
    print(find([7, 3, 1, 5, 2], 2), 3) # 3
    print(find([7, 3, 1, 5, 2], 1000), 5) # 5
    print(find([19, 4, 7, 17, 3, 15, 10], 5), 3) # 3
    print(find([10000, 987654, 123456, 139562, 13613225], 50000), 2) # 2