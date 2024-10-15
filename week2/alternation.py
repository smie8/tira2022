# Saat syötteenä listan, jossa on jokin lukujen 1…n permutaatio. 
# Tehtäväsi on laskea listan vuorottelevien osajonojen lukumäärä.

# Tässä vuorotteleva tarkoittaa sitä, että osajonossa seuraava luku
# on aina vuorotellen pienempi tai suurempi kuin edellinen. 
# Toisin ilmaistuna vuorotteleva osajono on sellainen, joka ei sisällä
# ainuttakaan vähintään kolmen pituista kasvavaa eikä vähenevää osajonoa.

# Tavoitteena on, että algoritmin aikavaativuus on O(n).

# Toteuta tiedostoon alternation.py funktio count, joka palauttaa
# vuorottelevien osajonojen lukumäärän.

def count(t):
    count = 0
    length = 0

    for i in range(len(t)):
        if length >= 2:
            # tarkistetaan onko sarja validi
            if t[i-2] < t[i-1] and t[i-1] > t[i]:
                length += 1
            elif t[i-2] > t[i-1] and t[i-1] < t[i]:
                length += 1
            else:
                length = 2
        else:
            length += 1

        count += length
    return count

if __name__ == "__main__":
    print(count([5,2,3])) # 6
    print(count([5,2,3,4])) # 8
    print(count([5,2,3,4,1])) # 11

    print(count([1,3,4])) # 5
    print(count([1,3,4,1])) # 8
    print(count([1,3,4,2,5])) # 12

    print(7, count([1,2,3,4])) # 7
    print(15, count([1,4,2,5,3])) # 15
    print(17, count([7,2,1,3,5,4,6])) # 17