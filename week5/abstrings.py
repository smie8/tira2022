# Annettuna on kaksi samanpituista merkkijonoa, jotka molemmat koostuvat merkeistä A ja B. 
# Tehtäväsi on laskea, moniko ensimmäisen merkkijonon osajono on toisen merkkijonon 
# samassa kohdassa olevan osajonon anagrammi.

# Kaiksi merkkijonoa ovat toistensa anagrammeja, jos niissä on jokaista merkkiä yhtä monta. 
# Voit olettaa, että merkkijonojen pituudet on enintään 10^5.
from collections import Counter

def count(a, b):
    count = 0
    firstDict = {}
    secondDict = {}

    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            subStringA = a[i:j]
            subStringB = b[i:j]

            if(Counter(subStringA) == Counter(subStringB)):
                count += 1

    return count


if __name__ == "__main__":
    print(count("AAA", "BBB")) # 0
    print(count("AB", "BA")) # 1
    print(count("AA", "AA")) # 3
    print(count("ABA", "BAB")) # 2
    print(count("AAABBB", "BBBAAA")) # 3
    print(count("AABABBBA", "BAABABAB")) # 13