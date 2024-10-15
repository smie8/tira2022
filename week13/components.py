class Components:
    def __init__(self,n):
        # luo n kaupunkia
        self.link = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.n = n
        self.components = n

    def find(self,x):
        while self.link[x] != x:
            x = self.link[x]
        return x

    def add_road(self,a,b ):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return

        if self.size[a] > self.size[b]:
            self.size[a] += self.size[b]
            self.link[b] = a
        else:
            self.size[b] += self.size[a]
            self.link[a] = b
        self.components -= 1

    def count(self):
        # montako komponenttia
        return self.components
        # visited = []
        # print("link",self.link)
        # for i in range(1, self.n + 1):
        #     if self.link[i] not in visited:
        #         visited.append(self.link[i])
        # print("visited", visited)
        # print("--")
        # return len(visited)

if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1,2)
    c.add_road(1,3)
    print(c.count()) # 3
    c.add_road(2,3)
    print(c.count()) # 3
    c.add_road(4,5)
    print(c.count()) # 2

    c = Components(5)
    c.add_road(4,5)
    c.add_road(2,3)
    print(c.count()) # 3
    print(c.count()) # 3
    c.add_road(4,5)
    c.add_road(3,4)
    c.add_road(2,5)
    c.add_road(4,5)
    print(c.count()) # 2
    c.add_road(3,4)