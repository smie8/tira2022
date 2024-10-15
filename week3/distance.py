# Annettuna on lista kokonaislukuja, jotka kaikki ovat väliltä 1…k. 
# Listalle halutaan lisätä uusi kokonaisluku väliltä 1…k, jonka etäisyys 
# lähimpään listalla jo valmiiksi olevaan lukuun on mahdollisimman suuri. 
# Kuinka suuri tuo etäisyys voi korkeintaan olla?

# Voit olettaa, että listalla on korkeintaan 10^5 lukua ja k on korkeintaan 10^9. 
# Tavoitteena on, että algoritmin aikavaativuus on O(n) tai O(n log n).

# Toteuta tiedostoon distance.py funktio find, joka ilmoittaa suurimman mahdollisen etäisyyden.

def find(t, k):
    t.sort()
    
    for i in range(0, len(t)):
        if i == 0:
            max_distance = t[0] - 1
            if i == len(t)-1:
                if k - t[i] > max_distance:
                    max_distance = k - t[i]
            continue
            
        ii = t[i]
        iiMinus = t[i-1]
        iiiErotus = abs(t[i] - t[i-1])
        if abs((t[i] - t[i-1]) // 2) > max_distance:
            max_distance = abs((t[i] - t[i-1]) // 2)

        if i == len(t)-1:
            if k - t[i] > max_distance:
                max_distance = k - t[i]

    return max_distance

if __name__ == "__main__":
    print(find([2, 11, 9, 10, 10], 15)) # 4
    print(find([14, 15, 6, 2, 7, 14], 15)) # 3
    print(find([3, 2, 2, 22, 2, 21, 13, 18, 14, 19], 30)) # 8
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970