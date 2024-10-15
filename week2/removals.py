# Sinulle annetaan merkkijono, joka koostuu vain merkeistä a, b tai c. 
# Voit kerätä merkkejä merkkijonosta poistamalla niitä joko merkkijonon 
# alusta tai lopusta. Kuinka monta merkkiä on vähintään poistettava, jotta 
# jokaista merkkiä a–c saadaan kerättyä vähintään k kappaletta?

# Voit olettaa, että merkkijono muodostuu merkeistä a–c, siinä on enintään 
# 105 merkkiä ja kutakin merkkiä on vähintään k kappaletta. Tavoitteena on, 
# että algoritmin aikavaativuus on O(n).

# Toteuta tiedostoon removals.py funktio find, joka kertoo, montako 
# merkkiä on vähintään poistettava.

def find(s, k):
    a = 0
    b = 0
    c = 0
    aa = []
    for i in range(len(s)):
        for j in range(i+j, len(s)):
            if s[j] == 'a' and a < k:
                a += 1
                aa.append(j)

if __name__ == "__main__":
    # print(find("abc", 1)) # 3
    print(find("aabca", 1)) # 3
    # print(find("aaaabbbcccc", 1)) # 6
    print(find("aabbaacc", 2)) # 6
    # print(find("aaaabbbbaaaccccaaccacbbaa", 3)) # 13


    # a = 0
    # b = 0
    # c = 0
    # leftRemovals = { 'a': [], 'b': [], 'c': [] }
    # rightRemovals = { 'a': [], 'b': [], 'c': [] }
    # i = 0
    # removals = 0

    # while (a+b+c < k*3):
    #     removals += 1
    #     if s[i] == 'a' and a < k:
    #         leftRemovals['a'].append(i)
    #         a += 1
    #     elif s[len(s)-1-i] == 'a' and a < k:  
    #         rightRemovals['a'].append(i)
    #         a += 1
        
    #     if s[i] == 'b' and b < k:
    #         leftRemovals['b'].append(i)
    #         b += 1
    #     elif s[len(s)-1-i] == 'b' and b < k:  
    #         rightRemovals['b'].append(i)
    #         b += 1
    #     if s[i] == 'c' and c < k:
    #         leftRemovals['c'].append(i)
    #         c += 1
    #     elif s[len(s)-1-i] == 'c' and c < k: 
    #         rightRemovals['c'].append(i)
    #         c += 1

    #     i += 1

    # print(leftRemovals)
    # print(rightRemovals)

    # # näillä saadaan parhaiden poistojen indeksit, mutta vain yhdelle sarjalle abc:ta
    # leftRemovals = { 'a': 0, 'b': 0, 'c': 0 }
    # rightRemovals = { 'a': 0, 'b': 0, 'c': 0 }
    # removalCount = 0
    #
    # for i in range(len(s)):
    #     if s[i] == 'a' and leftRemovals['a'] == 0:
    #         leftRemovals['a'] = i + 1
    #     if s[i] == 'b' and leftRemovals['b'] == 0:
    #         leftRemovals['b'] = i + 1
    #     if s[i] == 'c' and leftRemovals['c'] == 0:
    #         leftRemovals['c'] = i + 1

    # for i in range(len(s)):
    #     if s[len(s)-i-1] == 'a' and rightRemovals['a'] == 0:
    #         rightRemovals['a'] = i + 1
    #     if s[len(s)-i-1] == 'b' and rightRemovals['b'] == 0:
    #         rightRemovals['b'] = i + 1
    #     if s[len(s)-i-1] == 'c' and rightRemovals['c'] == 0:
    #         rightRemovals['c'] = i + 1


    # def find(s, k):
    # a = 0
    # b = 0
    # c = 0
    # leftRemovals = 0
    # rightRemovals = 0
    # removals = 0
    # i = 0

    # # for i in range(len(s)):
    # while (a+b+c < k*3):
    #     removals += 1

    #     if s[i] == 'a' and a < k:
    #         a += 1
    #         leftRemovals = removals
    #     elif s[len(s)-1-i] == 'a' and a < k:  
    #         a += 1
    #         rightRemovals = removals
        
    #     if s[i] == 'b' and b < k:
    #         b += 1
    #         leftRemovals = removals
    #     elif s[len(s)-1-i] == 'b' and b < k:  
    #         b += 1
    #         rightRemovals = removals

    #     if s[i] == 'c' and c < k:
    #         c += 1
    #         leftRemovals = removals
    #     elif s[len(s)-1-i] == 'c' and c < k:  
    #         c += 1
    #         rightRemovals = removals
        
    #     print(a,b,c)
    #     print('i: ',i)
    #     print(leftRemovals, rightRemovals)

    #     i += 1

    # print('----')
    # return leftRemovals + rightRemovals