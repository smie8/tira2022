n = 1000
graph = [[] for _ in range(n + 1)]

def add_edge(a, b):
    graph[a].append(b)
    graph[b].append(a)

for i in range(2, n + 1):
    for j in range(2, n + 1):
        if i % j == 0:
            add_edge(i, j)

count = 0
setti = set()

def depthFirstSearch(x):
    global count
    global setti

    setti.add(x)

    if visited[x]:
        return

    visited[x] = True
    # print('tultiin solmuun', x)
    count += 1

    for y in graph[x]:
        depthFirstSearch(y)

visited = [False] * (n + 1)

depthFirstSearch(2)

print('count', count)
print(len(setti))