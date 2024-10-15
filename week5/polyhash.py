# Tarkastellaan kurssikirjan mukaista polynomista hajautusta, jossa A=19 ja modulo N=10^6. 
# Tällöin esimerkiksi merkkijonon aybabtu hajautusarvo on 532916.

def polynomicalHash(word):
    sum = 0
    a = 19
    for i in range(len(word)):
        char = ord(word[i])
        power = len(word)-i-1
        sum += pow(a, power) * char

    return sum % 1000000

print(polynomicalHash("aybabtu")) # 532916

# Laske hajautusarvo seuraaville merkkijonoille:
print(polynomicalHash("maanantai")) # 190950
print(polynomicalHash("tiistai")) # 828905
print(polynomicalHash("keskiviikko")) # 528032
print(polynomicalHash("torstai")) # 858388
print(polynomicalHash("perjantai")) # 242610
print(polynomicalHash("lauantai")) # 741303
print(polynomicalHash("sunnuntai")) # 206849