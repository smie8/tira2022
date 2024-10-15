# Tehtäväsi on muokata annettua merkkijonoa seuraavalla tavalla:
# 1. Etsi merkkijonosta ensimmäinen kohta, jossa kaksi vierekkäistä merkkiä ovat yhtäsuuria.
# 2. Jos tällaista kohtaa ei ole, lopeta.
# 3. Poista nämä kaksi merkkiä merkkijonosta ja korvaa ne yhdellä merkillä, joka on aakkosissa tasan yhtä suurempi kuin poistetut merkit. Kuitenkin jos uusi merkki olisi suurempi kuin z, siitä tulee merkki a.
# 4. Palaa takaisin kohtaan 1.

# Merkkijono muodostuu merkeistä a–z ja siinä on enintään 10^5 merkkiä.

# Toteuta tiedostoon chars.py funktio solve, joka palauttaa muokatun merkkijonon.

from collections import deque

def solve(s):
    s = deque(s)
    ret = deque()

    while True:
        # jos palautettavan jonon kaksi viimeistä kirjainta ovat samat, poistetaan ne ja korvataan aakkosten seuraavalla kirjaimella
        if len(ret) > 1 and ret[-1] == ret[len(ret) - 2]:
            next = getNextChar(ret[-1])
            ret.pop()
            ret.pop()
            ret.append(next)
            continue

        # jos s on käyty läpi, olemme valmiit
        if len(s) == 0:
            break

        # jos s-jonon ensimmäinen alkio on sama kuin palautettavan jonon, poistetaan ne ja lisätään palautusjonoon aakkosten seuraava kirjain
        if len(ret) > 0 and s[0] == ret[-1]:
            next = getNextChar(s[0])

            s.popleft()
            ret.pop()

            ret.append(next)
        # muussa tapauksessa "siirretään" kirjain s-jonosta palautusjonon hännille
        else: 
            ret.append(s[0])
            s.popleft()

    return ''.join(ret)

def getNextChar(char):
    startOfAlphabetUnicodes = 97
    alphabetCount = 26
    charUnicode = ord(char)

    return chr((charUnicode + 1 - startOfAlphabetUnicodes) % alphabetCount + startOfAlphabetUnicodes)

if __name__ == "__main__":
    print(solve("auto")) # auto
    print(solve("ddqqirr")) # eris
    print(solve("aaaaaa")) # cb
    print(solve("wsstuva")) # xa
    print(solve("zzzzzzzz")) # c
    print(solve("mlkjihgfedcbb")) # n
    print(solve("kkkjjiikjkjiikjjiijkjji")) # mjkjmlki

    s = 'a' * 10**5
    print(solve(s)) # qpkjhf

    s = 'zq'*10**4 + 'ee'*10**4 + 'bb'*10**4 + 'yy'*10**4 + 'nn'*10**4
    print(solve(s))