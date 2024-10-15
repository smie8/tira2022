# Tehtäväsi on laskea, moniko merkkijonon osajono ei sisällä kiellettyä merkkiä. 
# Syötteenä sinulle annetaan merkkijono ja merkki, jota osajonot eivät saa sisältää.

# Voit olettaa, että merkkijono muodostuu merkeistä a–z, siinä on enintään 105 merkkiä
# ja kielletty merkki on jokin merkeistä a–z. Tavoitteena on, että algoritmin 
# aikavaativuus on O(n).

# Toteuta tiedostoon forbidden.py funktio count, joka palauttaa halutun tuloksen.

def count(s, c):
    count = 0
    length = 0

    for i in range(len(s)):
        if s[i] != c:
            length += 1
        else:
            length = 0
        count += length

    return count

if __name__ == "__main__":
    print(count("abacabb", "b")) # 7
    print(count("abcdef", "g")) # 21
    print(count("xxxxxxxxx", "x")) # 0
    print(count("pupujussikainen", "u")) # 48