# Annettuna on lista, jossa on jokin lukujen 1…n permutaatio, 
# ja tehtäväsi on selvittää, montako kierrosta kuplajärjestämisalgoritmi 
# tarvitsee listan järjestämiseen. Huomaa, että tässä lasketaan vain kierrokset, 
# joiden aikana listan järjestys muuttuu.

# Voit olettaa, että listalla on enintään 10^5 lukua. Tavoitteena on, että algoritmin 
# aikavaativuus on O(n) tai O(nlogn).

def count(t):
    result = 0

    for i in range(len(t)):
        diff = (t[i]-1) - i
        if diff < result:
            result = diff

    return abs(result)

    
if __name__ == "__main__":
    print(count([1, 2, 3])) # 0
    print(count([2, 3, 4, 1])) # 3
    print(count([5, 1, 2, 3, 4])) # 1
    print(count([6, 2, 4, 1, 5, 3])) # 3
    print(count([2, 7, 4, 1, 9, 3, 8, 6, 5, 10])) # 4

    a = list(range(10**5, 0, -1))
    print(count(a))