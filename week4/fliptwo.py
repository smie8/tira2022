# Aluksi listan sisältö on [1,2,3,...,n]. Joka askeleella otat listan kaksi ensimmäistä 
# alkiota ja siirrät ne listan loppuun käänteisessä järjestyksessä. 
# Mikä on listan ensimmäinen alkio k askeleen jälkeen?

# Esimerkiksi kun n=4 ja k=3, lista muuttuu näin:

# [1,2,3,4]→[3,4,2,1]→[2,1,4,3]→[4,3,1,2]

# Tässä tapauksessa listan ensimmäinen alkio on siis 4.

# Voit olettaa, että n on välillä 2…10^5 ja k on enintään 10^5. Tavoitteena on, että 
# algoritmin aikavaativuus on O(n+k).

# Toteuta tiedostoon fliptwo.py funktio solve, joka palauttaa ensimmäisen alkion k askeleen jälkeen.

from collections import deque

def solve(n,k):
    list = deque()
    for i in range(1, n + 1):
        list.append(i)

    for i in range(k):
        first = list.popleft()
        second = list.popleft()

        list.append(second)
        list.append(first)
    
    return list[0]
       

if __name__ == "__main__":
    print(solve(4,3)) # 4
    print(solve(12,5)) # 11
    print(solve(99,555)) # 11
    print(solve(12345,54321)) # 9875