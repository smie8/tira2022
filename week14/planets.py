class Planets:
    def __init__(self,n):
        self.n = n
        self.graph = [[0] * (n + 1) for _ in range(n + 1)]
        self.found = False 
        self.result = []
        self.visited = [False] * (self.n + 1)
        self.weight = 0

    def add_teleport(self,a,b):
        self.graph[a][b] += 1

    def dfs(self, a, b, path):
        if self.visited[a]:
            return
        path.append(a)
        self.visited[a] = True

        if a == b and not self.found:
            self.found = True # polku on löytynyt
            self.result = path[:] # otetaan polku muistiin
            print("TÄYDENNYSPOLKU LÖYTYI: ",path)

        for i in range(1, self.n+1):
            if self.graph[a][i] > 0:
                self.dfs(i, b, path)

        path.pop()

    def calculate(self):
        # muistikokeilut ->
        # self.weight = 0
        # key = (a, b)
        # if key in self.memory:
        #     self.weight = self.memory[a,b]
        # <- muistikokeilut¨

        a = 1
        b = self.n

        while True:
            self.found = False
            path = [] # täydennyspolku = augmenting path
            self.visited = [False] * (self.n + 1)

            self.dfs(a,b,path)

            if not self.found:
                break
            
            min_weight = 10**9

            # etsitään minimipaino
            for i in range(len(self.result)-1):
                # tulostetaan ensin täydennyspolun kaaret ja niiden painot
                print("kaari: a, b, paino:", self.result[i], self.result[i+1], self.graph[self.result[i]][self.result[i+1]])
                min_weight = min(min_weight, self.graph[self.result[i]][self.result[i+1]])

            # muutetaan kaaret minimipainon mukaan (virtauskaaret vähentyvät, vastakkaiset lisääntyvät)
            for i in range(len(self.result)-1):
                self.graph[self.result[i]][self.result[i+1]] -= min_weight
                self.graph[self.result[i+1]][self.result[i]] += min_weight

            self.weight += min_weight

        # toista yllä oleva niin kauan kuin virtauksia löytyy (päädytään loppusolmuun)
        # sitten kerää kaikki kaaret kasaan, summaa niiden minimipainot ja palauta ne

        # muistikokeilut ->
        # self.memory[a,b] = self.weight
        # <- muistikokeilut

        return self.weight

if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1,2)
    p.add_teleport(2,5)
    print(p.calculate()) # 1
    p.add_teleport(1,5)
    print(p.calculate()) # 2