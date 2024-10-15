import math

class AllRoutes:
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

    def get_table(self):
        table = []

        for i in range(self.n):
            distances = [float("Inf")] * (self.n + 1)
            distances[i + 1] = 0

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

            for i in range(len(distances)):
                if math.isinf(distances[i]):
                    distances[i] = -1
            distances.pop(0)
            table.append(distances)

        return table

if __name__ == "__main__":
    a = AllRoutes(4)
    a.add_road(1,2,2)
    a.add_road(1,3,5)
    a.add_road(2,3,1)
    print(a.get_table())
    # [[0,2,3,-1],[2,0,1,-1],[3,1,0,-1],[-1,-1,-1,0]]

    a = AllRoutes(5)
    a.add_road(3,4,6)
    a.add_road(4,5,5)
    a.add_road(4,5,6)
    a.add_road(1,5,7)
    a.add_road(1,4,7)
    a.add_road(4,5,1)
    a.add_road(3,4,8)
    a.add_road(2,3,6)
    a.add_road(4,5,4)
    print(a.get_table())
