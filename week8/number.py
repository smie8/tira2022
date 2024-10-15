def search(n, sum):
    global count, lista
    if sum == n:
        count += 1
    else:
        for i in range(1, n+1):
            if sum < n:     
                lista.append(i)
                count = search(n, sum + 1)
def count(n):
    # kaksi tapaa ovat erilaiset kun ne järjestetään pienimmästä suurimpaan

    # tarkista aina mikä on tavoite eli jäljellä oleva summa, esim: "4 lisää vielä"
    # mikä on pienin luku mikä voidaan listätä (se mikä on viimeksi lisätty)

    global count, lista
    count = 0
    lista = []
    search(n, 0)
    return count

def add_next(seq, m):
    s = sum(seq)
    count = 1 if s == m else 0
    if s < m:
        for i in [f for f in [3,5,7,9] if s + f <= m]:
            count += add_next(seq + [i], m)
    return count

print(add_next([], 15))

if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(7)) # 15
    print(count(8)) # 22
    print(count(42)) # 53174


    # 1 = 1
    # 2 = 1,    1 + 1,2
    # 3 = 3,    1 + 1 + 1, 1 + 2,3
    # 4 = 5,    1+1+1+1,1+1+2,1+3,2+2,4
    # 5 = 7,    
    # 6 =       1+1+1+1+1+1, 1+1+1+1+2, 1+1+1+3, 1+1+4, 1+5, 6, 2+2+2, 1+1+2+3, 2+2+