# Tehtäväsi on laskea, monessako merkkijonon osajonossa jokainen merkki on sama.
# Esimerkiksi merkkijonossa abbbcaa tällaiset osajonot ovat:
# - a (kolmesti)
# - aa
# - b (kolmesti)
# - bb (kahdesti)
# - bbb
# - c
# eli yhteensä 11 osajonoa.

# Voit olettaa, että merkkijono muodostuu merkeistä a–z ja siinä on enintään 105 merkkiä. 
# Tavoitteena on, että algoritmin aikavaativuus on O(n).

# Toteuta tiedostoon onechar.py funktio count, joka palauttaa halutun tuloksen.
import math

def count(s):
    count = 0
    length = 0

    for i in range(len(s)):
        if i != 0 and s[i] == s[i-1]:
            length += 1
        else:
            length = 1
        
        count += length

# O(N^2) solution:
    # for i in range(len(s)):
    #     for j in range(i, len(s)):
    #         if i != j and s[i] != s[j]:
    #             break
    #         count += 1

    return count

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5