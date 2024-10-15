# Tehtäväsi on salata annettu merkkijono niin, että ensimmäinen merkki liikkuu aakkosissa
# yhden merkin eteenpäin, toinen merkki kaksi merkkiä eteenpäin, kolmas merkki kolme merkkiä 
# eteenpäin, jne. Jos merkki kasvaa suuremmaksi kuin z, se palaa taas aakkosten alkuun.

# Merkkijono muodostuu merkeistä a–z ja siinä on enintään 100 merkkiä.

# Toteuta tiedostoon encryption.py funktio encrypt, joka tuottaa salatun merkkijonon.

def nextChar(char, steps):
    startOfAlphabetUnicodes = 97
    alphabetCount = 26
    charUnicode = ord(char)

    return chr((charUnicode + steps - startOfAlphabetUnicodes) % alphabetCount + startOfAlphabetUnicodes)

def encrypt(s):
    encrypted = ""
    for x in range(len(s)): 
        char = s[x]
        encrypted += nextChar(char, x+1)
    return encrypted

if __name__ == "__main__":
    print(encrypt("abc")) # bdf
    print(encrypt("xz")) # yb
    print(encrypt("kkkkkkkk")) # lmnopqrs
    print(encrypt("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")) # bcdefghijklmnopqrstuvwxyzabcde