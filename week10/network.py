from collections import deque

class Network:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.queue = deque()

    def add_link(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def wfs(self,x):
        self.queue.append(x)
        self.seen[x] = True
        self.distance[x] = 0
        while self.queue:
            node = self.queue.popleft()
            for y in self.graph[node]:
                if self.seen[y]:
                    continue
                self.queue.append(y)
                self.seen[y] = True
                self.distance[y] = self.distance[node] + 1

    def best_route(self,a,b):
        # min connections in a route, return -1 if no connection
        self.seen = [False for _ in range(self.n+1)]
        self.distance = [-1 for _ in range(self.n + 1)]
        self.wfs(a)
        return self.distance[b]


if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2