def search(result, s, n):
    if len(s) == n:
        result.append(s)
    else:
        if len(s) == 0 or s[-1] != 'A':
            search(result, s+'A', n)
        if len(s) == 0 or s[-1] != 'B':
            search(result, s+'B', n)
        if len(s) == 0 or s[-1] != 'C':
            search(result, s+'C', n)

def create(n):
    result = []
    search(result, '', n)
    return result

if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(len(create(5))) # 48
