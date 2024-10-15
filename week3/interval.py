# Annettuna on lista, josta tulee poimia mahdollisimman monta lukua. 
# Ensimmäinen luku saa olla mikä tahansa listan luku ja tämän jälkeen seuraavan 
# poimitun luvun tulee olla tasan yhden suurempi kuin edellinen. 
# Kuinka monta lukua voidaan näin korkeintaan poimia?

# Voit olettaa, että listalla on enintään 105 lukua ja että jokainen luku on 
# väliltä 1…109. Tavoitteena on, että algoritmin aikavaativuus on O(n) tai O(nlogn).

# Toteuta tiedostoon interval.py funktio count, joka ilmoittaa, montako lukua 
# listalta voidaan enintään poimia halutulla tavalla.

def count(t):
    t.sort()
    length = 1
    count = 1

    for i in range(1, len(t)):
        if t[i] - t[i-1] == 1:
            length += 1
        elif t[i] - t[i-1] == 0:
            continue
        else:
            length = 1

        if length > count:
            count = length

    return count

if __name__ == "__main__":
    print(count([14, 15, 16, 15, 13])) # 4
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3