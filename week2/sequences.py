# Tehtäväsi on laskea, moniko annetun merkkijonon osajono sisältää
# merkkijonon tira alijonona.

# Merkkijono sisältää jonon tira alijonona silloin, kun merkkijonosta
# voidaan muodostaa merkkijono tira poistamalla siitä mahdollisesti 
# osa merkeistä muuttamatta merkkien järjestystä. Esimerkiksi 
# taikurinhattu sisältää sanan tira alijonona, mutta ritari ei sisällä.

# Voit olettaa, että merkkijono muodostuu merkeistä a–z ja siinä on 
# enintään 105 merkkiä. Tavoitteena on, että algoritmin aikavaativuus on O(n).

# Toteuta tiedostoon sequences.py funktio count, joka palauttaa sellaisten
# osajonojen määrän, joilla on tira alijonona.


def count(s):


def count3(s):
    count = 0
    counter = 0
    tira = 0

    chars = { 't': 0, 'i': 0, 'r': 0, 'a': 0 }


    for i in range(len(s)):
        if s[i] == 't':
            chars['t'] += 1
        if s[i] == 'i' and chars['t'] > 0 and chars['t'] - chars['i'] > 0:
            chars['i'] += 1
        if s[i] == 'r' and chars['t'] > 0 and chars['i'] > 0 and chars['t'] - chars['i'] >= 0 and chars['i'] - chars['r'] > 0:
            chars['r'] += 1
        if s[i] == 'a' and chars['t'] > 0 and chars['i'] > 0 and chars['r'] > 0 and chars['t'] - chars['i'] >= 0 and chars['i'] - chars['r'] >= 0 and chars['r'] - chars['a'] > 0:
            chars['a'] += 1
            tira += 1

        if tira > 0:
            count += tira

    return count

if __name__ == "__main__":
    print(count("ritari"), 0) # 0
    print(count("taikurinhattu"), 4) # 4
    print(count("ttiirraa"), 4) # # 4
    print(count("tixratiyra"), 11) # 11 
    # print(count("aotiatraorirratap")) # 42


def count2(s):
    count = 0
    chars = { 't': 0, 'i': 0, 'r': 0, 'a': 0 }
    counter = 0
    tira = 0
    order = 0

    for i in range(len(s)):
        if s[i] == 't':
            chars['t'] += 1
        elif s[i] == 'i':
            chars['i'] += 1
        elif s[i] == 'r':
            chars['r'] += 1
        if s[i] == 'a':
            chars['a'] += 1

        print(chars)

        # tarkistetaan löytyykö täysi tira-sarja
        for x in chars:
            if chars[x] > 0:
                counter += 1

        if counter == 4:
            # siistitään dictionary ja kasvatetaan tira-lukua
            for x in chars:
                chars[x] -= 1
            tira += 1
            print('tira++')
        counter = 0
        
        if tira > 0:
            count += 1 * tira

    print('tira count:',tira)

    return count