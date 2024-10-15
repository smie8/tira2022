import random
import time

# luodaan kaarilista, jossa
# - n solmua
# - solmusta a on kaari solmuun b, jos a < b ja b - a < 10
# - jokaisen kaaren paino on satunnainen kokonaisluku välillä 1-1000
# - kaaret ovat satunnaisessa järjestyksessä

n = 5000
edge_list = []

for i in range(1, n+1):
    for j in range(1, n+1):
        if i < j and j - i < 10:
            edge_list.append((i, j, random.randint(1, 1000)))

random.shuffle(edge_list)

# suoritetaan Bellman-Ford-algoritmi suunnatussa verkossa, aloitussolmusta 1

# tehdään etäisyysluettelo, missä aluksi jokaisen solmun (paitsi aloitussolmun) etäisyys on "ääretön"
distance = [float("Inf")] * (n + 1) 
distance[1] = 0 # aloitussolmusta 1 etäisyys itseensä on 0

start_time = time.time()

while True:
    change = False

    for edge in edge_list:
        current = distance[edge[1]] # etäisyys loppu 
        new = distance[edge[0]] + edge[2] # etäisyys alku + paino
        if new < current:
            distance[edge[1]] = new
            change = True

    if not change:
        break

end_time = time.time()

print('aikaa kului:', end_time - start_time, 'sekuntia')