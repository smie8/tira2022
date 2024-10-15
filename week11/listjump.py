from heapq import heappush, heappop
import math

def calculate(t):
    # lyhin matka ensimmäisestä solmusta viimeiseen
    n = len(t)
    graph = [[] for _ in range(n + 1)]

    # täytä verkko
    for i in range(len(t)):
        item = t[i]
        node = i + 1

        if n - i - item > 0:
            graph[node].append((item + node, item))
        if i - item >= 0:
            graph[node].append((node - item, item))

    distance = [float("Inf")] * (n + 1)
    distance[1] = 0
    ready = [False] * (n + 1)
    heap = []
    heappush(heap, (0, 1))

    while len(heap) > 0:
        d, x = heappop(heap)
        if ready[x]:
            continue
        ready[x] = True

        for y in graph[x]:
            new = distance[x] + y[1]
            current = distance[y[0]]
            if new < current:
                distance[y[0]] = new
                heappush(heap, (distance[y[0]], y[0]))

    if math.isinf(distance[-1]):
        return -1
    return distance[-1]

if __name__ == "__main__":
    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32