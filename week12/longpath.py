# käy läpi vaikka viimeisestä solmusta takaperin rekursiolla siihen liitettyjä solmuja läpi, 
# kunnes ei enää pääse eteenpäin. 
#
# Sieltä sitten palauta polun siihen astisia pituusarvoja rekursiopolkua takaisinpäin 
# tullessa ja tallenna ne listaan, sanakirjaan, mihin vaan. 
# 
# Lopulta saat lähtösolmun (viimeisen solmun) viereisten solmujen pisimmät polut tallennettua. Siitä on suht helppo jatkaa. 
class LongPath:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.memory = {}

    def add_edge(self, a, b):
        if a > b:
            self.graph[a].append(b)
        if b > a:
            self.graph[b].append(a)

    def calculate(self):
        longestPath = 0
        self.memory.clear()

        def search(x):
            nonlocal longestPath

            if x in self.memory:
                return self.memory[x]

            if x == 1:
                return 0

            pathLength = 0
            for y in self.graph[x]:
                
                pathLength = max(pathLength, search(y) + 1)
            # print("solmuun", x, "pisin polku on", pathLength)
            
            longestPath = max(pathLength, longestPath)
            
            self.memory[x] = pathLength

            return pathLength

        for x in range(1, self.n + 1):
            search(x)
            
        return longestPath

class LongPath2:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.memory = {} # "cache"

    def add_edge(self, a, b):
        if a < b:
            self.graph[a].append(b)
        if b < a:
            self.graph[b].append(a)

    def calculate(self):
        longestPath = 0

        for i in range(1, self.n + 1):
            result = self.search(i)

            if result > longestPath:
                longestPath = result

        return longestPath

    def search(self, node):
        if node in self.memory:
            return self.memory[node]
        
        length = 0

        for neighbor in self.graph[node]:
            if neighbor > node:
                path = self.search(neighbor) + 1
                length = max(path, length)

        self.memory[node] = length

        return length

    def calculate2(self):
        longestPath = 0

        # etsitään dfs:llä pisin polku, missä jokaisen solmun arvo on enemmän kuin aiemman
        def dfs(node, parent, length):
            nonlocal longestPath

            if node in self.memory:
                current = self.memory[node]
                self.memory[node] = max(current, length)
            else:
                self.memory[node] = length

            # päivitä pisin polku tarvittaessa
            longestPath = max(longestPath, length)

            if longestPath == self.n:
                return

            # käy läpi naapurisolmut
            for neighbor in self.graph[node]:
                # vain jos naapuri on arvoltaan suurempi
                if neighbor > node:
                    dfs(neighbor, node, length + 1)

            # self.memory[(node, parent)] = longestPath
            # self.memory[node] = length

        # suorita dfs jokaiselle verkon solmulle
        for i in range(1, self.n + 1):
            dfs(i, -1, 0) # päivittää longestPathin tarvittaessa

        print(self.memory)
        return longestPath

class LongPath3:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]
        self.memory = {}

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def calculate(self):
        longestPath = 0

        # etsitään dfs:llä pisin polku, missä jokaisen solmun arvo on enemmän kuin aiemman
        def dfs(node, length):
            nonlocal longestPath

            if node in self.memory:
                self.memory[node] = max(self.memory[node], length)
            else:
                self.memory[node] = length

            # päivitä pisin polku tarvittaessa
            longestPath = max(longestPath, length)

            # käy läpi naapurisolmut
            for neighbor in self.graph[node]:
                # dfs vain jos naapuri on arvoltaan suurempi
                if neighbor > node:
                    # TODO: voiko tässä hyödyntää memoa?
                    dfs(neighbor, length + 1)

        # suorita dfs jokaiselle verkon solmulle
        for i in range(1, self.n + 1):
            dfs(i, 0)

        print(self.memory)
        return longestPath

if __name__ == "__main__":
    l = LongPath(5)
    print(l.calculate()) # 0
    l.add_edge(3,5)
    print(l.calculate()) # 1
    # print(l.calculate())
    # l.add_edge(3,4)
    # print(l.calculate())
    # l.add_edge(5,4)
    # l.add_edge(1,2)
    # l.add_edge(3,1)
    # print(l.calculate())

    l = LongPath(4)
    l.add_edge(1,2)
    l.add_edge(1,3)
    l.add_edge(2,4)
    l.add_edge(3,4)
    print(l.calculate()) # 2
    l.add_edge(3,2)
    print(l.calculate()) # 3

    l = LongPath(5)
    l.add_edge(4,5)
    l.add_edge(3,4)
    l.add_edge(2,3)
    l.add_edge(1,2)
    print(l.calculate()) # 4

    print("LongPath(5)")

    l = LongPath(5)
    l.add_edge(2,4)
    print(l.calculate()) # 1
    l.add_edge(5,4)
    print(l.calculate()) # 2
    print(l.calculate()) # 2
    # print(l.calculate())
    # print(l.calculate())
    # print(l.calculate())
    # l.add_edge(4,5)
    # l.add_edge(4,5)

    print("---")

    l = LongPath(5)
    l.add_edge(4,3)
    print(l.calculate()) # 1
    l.add_edge(5,4)
    l.add_edge(2,3)
    print(l.calculate()) # 3
    l.add_edge(1,4)
    print(l.calculate()) # 3
    l.add_edge(5,3)
    l.add_edge(4,5)
    print(l.calculate())

    # l = LongPath(50)
    # l.add_edge(1,2)
    # l.add_edge(2,3)
    # l.add_edge(3,4)
    # l.add_edge(4,5)
    # l.add_edge(5,6)
    # l.add_edge(6,7)
    # l.add_edge(7,8)
    # l.add_edge(8,9)
    # l.add_edge(9,10)
    # l.add_edge(10,11)
    # l.add_edge(11,12)
    # l.add_edge(12,13)
    # l.add_edge(13,14)
    # l.add_edge(14,15)
    # l.add_edge(15,16)
    # l.add_edge(16,17)
    # l.add_edge(17,18)
    # l.add_edge(18,19)
    # l.add_edge(19,20)
    # l.add_edge(20,21)
    # l.add_edge(21,22)
    # l.add_edge(22,23)
    # l.add_edge(23,24)
    # l.add_edge(24,25)
    # l.add_edge(25,26)
    # l.add_edge(26,27)
    # l.add_edge(27,28)
    # l.add_edge(28,29)
    # l.add_edge(29,30)
    # l.add_edge(30,31)
    # l.add_edge(31,32)
    # l.add_edge(32,33)
    # l.add_edge(33,34)
    # l.add_edge(34,35)
    # l.add_edge(35,36)
    # l.add_edge(36,37)
    # l.add_edge(37,38)
    # l.add_edge(38,39)
    # l.add_edge(39,40)
    # l.add_edge(40,41)
    # l.add_edge(41,42)
    # l.add_edge(42,43)
    # l.add_edge(43,44)
    # l.add_edge(44,45)
    # l.add_edge(45,46)
    # l.add_edge(46,47)
    # l.add_edge(47,48)
    # l.add_edge(48,49)
    # l.add_edge(49,50)
    # l.add_edge(1,3)
    # l.add_edge(2,4)
    # l.add_edge(3,5)
    # l.add_edge(4,6)
    # l.add_edge(5,7)
    # l.add_edge(6,8)
    # l.add_edge(7,9)
    # l.add_edge(8,10)
    # l.add_edge(9,11)
    # l.add_edge(10,12)
    # l.add_edge(11,13)
    # l.add_edge(12,14)
    # l.add_edge(13,15)
    # l.add_edge(14,16)
    # l.add_edge(15,17)
    # l.add_edge(16,18)
    # l.add_edge(17,19)
    # l.add_edge(18,20)
    # l.add_edge(19,21)
    # l.add_edge(20,22)
    # l.add_edge(21,23)
    # l.add_edge(22,24)
    # l.add_edge(23,25)
    # l.add_edge(24,26)
    # l.add_edge(25,27)
    # l.add_edge(26,28)
    # l.add_edge(27,29)
    # l.add_edge(28,30)
    # l.add_edge(29,31)
    # l.add_edge(30,32)
    # l.add_edge(31,33)
    # l.add_edge(32,34)
    # l.add_edge(33,35)
    # l.add_edge(34,36)
    # l.add_edge(35,37)
    # l.add_edge(36,38)
    # l.add_edge(37,39)
    # l.add_edge(38,40)
    # l.add_edge(39,41)
    # l.add_edge(40,42)
    # l.add_edge(41,43)
    # l.add_edge(42,44)
    # l.add_edge(43,45)
    # l.add_edge(44,46)
    # l.add_edge(45,47)
    # l.add_edge(46,48)
    # l.add_edge(47,49)
    # l.add_edge(48,50)
    # print(l.calculate())