# Listalla on aluksi kokonaisluku 1. Joka kierroksella poistat listalta 
# pienimmän alkion x ja lisäät listalle alkiot 2x ja 3x. Mikä on listan 
# pienin alkio n kierroksen jälkeen? Voit olettaa, että n on enintään 10^5.

# Esimerkiksi kun n=5, lista muuttuu näin:
# [1]→[2,3]→[3,4,6]→[4,6,6,9]→[6,6,9,8,12]→[6,9,8,12,12,18]
# Tässä tapauksessa listan pienin alkio lopussa on 6.

from heapq import heappush, heappop

def smallest(n):
    heap = [1]

    for i in range(1, n+1):
        smallest = heappop(heap)
        heappush(heap, smallest*2)
        heappush(heap, smallest*3)

    return heappop(heap)

if __name__ == "__main__":
    print(smallest(1)) # 2
    print('')
    print(smallest(5)) # 6
    print(smallest(123)) # 288
    print(smallest(55555)) # 663552