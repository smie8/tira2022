def anagram(s, remaining):
    global result
    if remaining == '' and s not in result:
        result.append(s)
        result.sort()

    for char in remaining:
        newStr = s + char
        index = remaining.index(char)
        newRemaining = remaining[0:index:] + remaining[index+1::]
        anagram(newStr, newRemaining)

def create(s):
    global result
    result = []
    anagram('', s)
    return result

if __name__ == "__main__":
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("abac"))) # 12
    print(len(create("aybabtu"))) # 1260