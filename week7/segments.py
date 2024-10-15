# Annettuna on lista lukuja ja luku x. Tehtäväsi on selvittää pisimmän yhtenäisen osavälin pituus, 
# jossa viimeinen luku on suurempi tai yhtä suuri kuin ensimmäinen luku. Lisäksi viimeisen ja 
# ensimmäisen luvun erotus saa olla korkeintaan x.

# Voit olettaa, että listan pituus on korkeintaan 10^5 ja x sekä listan sisältämät luvut ovat 
# korkeintaan 10^9.

def find(t, x):
    length = 1
    longest = 1

    for i in range(len(t)):
        for j in range(i+1, len(t)):
            if t[i] <= t[j] and t[j] - t[i] <= x:
                length = j - i + 1
                if length > longest:
                    longest = length
            else:
                length = 1

    return longest

if __name__ == "__main__":
    print(find([1, 4, 6], 1)) # 1
    print(find([1, 4, 6], 10)) # 3
    print(find([4, 1, 10, 5, 14], 1)) # 4
    print(find([4, 1, 10, 5, 14], 10)) # 5
    print(find([9, 8, 7, 6, 5, 4, 3, 2, 1], 100)) # 1

    a = list(range(10**5, 0, -1))
    print(find(a,40000))