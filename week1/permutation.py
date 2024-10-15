# Tehtäväsi on järjestää luvut 1…n siten, että kaikkien vierekkäisten lukuparien summat ovat erisuuria. 
# Voit antaa minkä tahansa kelvollisen ratkaisun.

# Voit olettaa, että n on välillä 1…100.

# Toteuta tiedostoon permutation.py funktio create, joka palauttaa listan luvuista 1…n, 
# jossa kaikkien vierekkäisten lukuparien summat ovat erisuuria.
import random 

def create(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
    return list

if __name__ == "__main__":
    print(create(6)) # [3, 1, 6, 2, 4, 5]
    # print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2]
    # print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10]