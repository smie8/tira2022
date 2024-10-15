class Cities:
    def __init__(self,n):
        # self.graph = [ [0]*(n+1) for i in range(n+1)]

        self.graph = [[] for _ in range(n + 1)] # n + 1 tyhjää listaa, voidaan käyttää näppärästi kun 0-indeksissäkin on lista
        self.visited = [False] * (n + 1)
        self.n = n

    def add_road(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a) 

    def has_route(self,a,b):
        global result
        result = False

        visited = [False] * (self.n + 1)
        dfs(a, b, self.graph, visited)

        return result


def dfs(a, b, graph, visited):
    global result
    if visited[a]:
        return
    visited[a] = True
    if a == b:
        print('löytyy kaupunki', a, b)
        result = True
    print('tultiin kaupunkiin', a)
    # kun tullaan uuteen solmuun, käydään rekursiolla läpi sen viereiset solmut
    for y in graph[a]:
        dfs(y, b, graph, visited)

if __name__ == "__main__":
    c = Cities(5)
    c.add_road(4,5)
    print(c.has_route(4,5)) # True ?
    print(c.has_route(3,5)) # False ?
    c.add_road(2,3)
    print(c.has_route(1,3)) # False ?
    c.add_road(3,5)
    c.add_road(1,3)
    print(c.has_route(1,5)) # True
    c.add_road(3,4)
    print(c.has_route(4,5)) # True ?
    # c = Cities(5)
    # c.add_road(1,2)
    # print(c.graph)
    # c.add_road(1,3)
    # print(c.graph)
    # c.add_road(4,5)
    # print(c.graph)
    # print(c.has_route(1,5)) # False
    # c.add_road(3,4)
    # print(c.graph)
    # print(c.has_route(1,5)) # True
