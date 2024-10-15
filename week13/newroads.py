class NewRoads:
    def __init__(self,n):
        self.link = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.components = n
        self.edges = []
        self.n = n

    # def find(self,x):
    #     while self.link[x] != x:
    #         x = self.link[x]
    #     return x

    def find(self, x):
        if self.link[x] != x:
            self.link[x] = self.find(self.link[x])
        return self.link[x]

    def add_road(self,a,b,x):
        self.edges.append((a, b, x))

    def union(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a

    def min_cost(self):
        cost = 0
        self.components = self.n
        self.link = list(range(self.n + 1))

        print("components", self.components)

        self.edges.sort(key=lambda x: x[2])
        print("edges", self.edges)
        print("link", self.link)

        for a,b,x in self.edges:

            print("a,b,x",a,b,x)
            print("find a ja b: ", self.find(a), self.find(b))
            # solmut ovat eri komponenteissa (find tuottaa eri tulokset), joten kaari otetaan mukaan puuhun
            if self.find(a) != self.find(b):
                self.union(a, b)
                cost += x
                self.components -= 1
                print("cost", cost)

        print("components", self.components)

        # jos kaikki solmut ovat samassa komponentissa
        if self.components == 1:
            return cost
        else:
            return -1

if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1,2,2)
    n.add_road(1,3,5)
    print(n.min_cost()) # -1
    n.add_road(3,4,4)
    print(n.min_cost()) # 11
    n.add_road(2,3,1)
    print(n.min_cost()) # 7