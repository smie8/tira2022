class BestRoute:
    def __init__(self,n):
        self.n = n
        self.graph = []

    def add_road(self,a,b,x):
        self.graph.append((a,b,x))
        self.graph.append((b,a,x))

    def find_route(self,a,b):
        print(self.graph)
        distances = [float("Inf")] * (self.n + 1)
        distances[a] = 0

        while True:
            change = False

            for edge in self.graph:
                current = distances[edge[1]]
                new = distances[edge[0]] + edge[2]
                if new < current:
                    distances[edge[1]] = new
                    change = True

            if not change:
                break

        if distances[b] != float("Inf"):
            return distances[b]
        else:
            return -1

if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1,2,2)
    print(b.find_route(1,3)) # -1
    b.add_road(1,3,5)
    print(b.find_route(1,3)) # 5
    b.add_road(2,3,1)
    print(b.find_route(1,3)) # 3

    b = BestRoute(5)
    print(b.find_route(3,4)) # -1
    b.add_road(3,5,7)
    print(b.find_route(3,4)) # -1
    print(b.find_route(1,4)) # -1
    b.add_road(3,4,6)
    print(b.find_route(4,5)) # 13
    b.add_road(4,5,4)
    b.add_road(1,2,7)
    b.add_road(1,3,4)
    print(b.find_route(3,4))