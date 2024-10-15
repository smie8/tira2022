# Annettuna on merkkijono, jossa on n merkkiä väliltä a–z.

# Tehtäväsi on selvittää, kuinka pitkä on lyhin merkkijono, joka muodostuu 
# merkeistä a–z eikä ole annetun merkkijonon yhtenäinen osajono.

# Voit olettaa, että n on enintään 10^5.

from re import A


def find(s):
    subQueues = set()

    # 1. luo setti 1-pituisista osajonoista
    # 2. tarkista setin pituus (jos alle 26^i, niin palauta osajonon pituus [1])
    # 3. palaa kohtaan 1 ja kasvata osajonon pituutta
    count = 1
    while True:
        for i in range(len(s)):
            subQueues.add(s[i:i+count])

        if len(subQueues) < pow(26, count):
            print('len subq', len(subQueues))
            return count

        subQueues.clear()

        count += 1
    
    print(subQueues)

    # tallennetaan osajonot settiin
    for i in range(len(s)+1):
        for j in range(i):
            subQueues.add(s[j:i])

    # for i in range(1, len(s)):
    #     count = 0
    #     for x in subQueues:
    #         if len(x) == i:
    #             count += 1
    #     if count < pow(26, i):
    #         return i

    return 0

if __name__ == "__main__":
    # print(find("zzz")) # 1
    # print(find("aybabtu")) # 1
    print(find("abcdefghijklmnopqrstuvwxyz")) # 2
    # s = 'a' * (10**5)
    # print(find(s))