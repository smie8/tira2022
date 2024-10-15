# Tehtäväsi on selvittää, kuinka pitkä on lyhin merkkijono, jota toistamalla voidaan 
# muodostaa annettu merkkijono. Esimerkiksi kun merkkijono on abcabcabcabc, 
# lyhin toistettava merkkijono on abc.

# Merkkijono muodostuu merkeistä a–z ja siinä on enintään 100 merkkiä.

# Toteuta tiedostoon repeat.py funktio find, joka antaa toistettavan merkkijonon pituuden.

def find(s):
    repeatLength = len(s)
    done = False
    valid = True
     
    for x in range(1, len(s)):
        # print('x: ' + str(x))

        if len(s) % x == 0:
            for i in range(0, len(s)-1, x):
                firstSub = s[i:i+x]
                secondSub = s[i+x:i+x+x]

                # print('iteration: ' + str(i))
                # print('firstSub:' + firstSub)
                # print('secondSub:' + secondSub)

                if firstSub != secondSub and firstSub and secondSub:
                    valid = False
                    break
                repeatLength = x

                if i == len(s)-x:
                    repeatLength = x
                    done = True
                    break
        if done or valid:
            return repeatLength

    if valid:
        return repeatLength
    else:
        return len(s)

    return repeatLength

if __name__ == "__main__":
    print(find('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')) # 1
    print(find("mmzxzj")) # 6

    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7