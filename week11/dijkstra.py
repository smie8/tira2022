import random
import time
from heapq import heappush, heappop

# vrt. bellman-fordiin: ei niin raa'an voiman tapa, käytetään vieruslistaa

# luodaan vieruslista, jossa
# - n solmua
# - solmusta a on kaari solmuun b, jos a < b ja b - a < 10
# - jokaisen kaaren paino on satunnainen kokonaisluku välillä 1-1000
# - kaaret ovat satunnaisessa järjestyksessä

n = 5000

edge_list = [[] for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j and j - i < 10:
            edge_list[i].append((j, random.randint(1, 1000)))

random.shuffle(edge_list)

# suoritetaan Dijkstran algoritmi suunnatussa verkossa, aloitussolmusta 1

distance = [float("Inf")] * (n + 1)
distance[1] = 0
ready = [False] * (n + 1) # taulukko missä tieto mitkä solmut käsitelty
heap = []
heappush(heap,(0, 1)) # solmuun yksi pääsee niin että matka on nolla

start_time = time.time()

while len(heap) > 0: # niin kauan kun keossa jotain
    d, x = heappop(heap) # haetaan aina keosta seuraava solmu (d = etäisyys (node[0]), x = solmu (node[1]))
    if ready[x]: # jos solmua ei käsitelty vielä
        continue

    # print('solmuun', x, 'on etäisyys', d)

    ready[x] = True # solmu x on nyt käsitelty

    for y in edge_list[x]: # käydään naapurisolmut läpi
        new = distance[x] + y[1]
        current = distance[y[0]]
        if new < current:
            distance[y[0]] = new
            heappush(heap, (distance[y[0]], y[0]))

end_time = time.time()

print('aikaa kului:', end_time - start_time, 'sekuntia')