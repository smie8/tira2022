from copy import deepcopy
# etsi maksimivirtaus, niin löydät vastauksen siihen montako paria voit muodostaa
class Ball:
    def __init__(self,n):
        self.n = n
        self.graph = [[0] * (2*n + 2) for _ in range(2*n + 2)]
        self.residual_graph = None
        self.found = False 
        self.visited = [False] * (2*self.n + 1)
        self.max_flow = 0
        self.path = []
 
    def add_pair(self,a,b):
        # TODO: tarvitaanko tähän tarkistusta että löytyykö sellaista kaarta jossa on jo a tai b käytössä
        self.graph[0][a] = 1 # kaari sourcesta a:han
        self.graph[a][self.n+b] = 1 # kaari a:sta b:hen
        self.graph[self.n+b][self.n*2+1] = 1 # kaari b:stä sinkkiin
 
    def dfs(self, a, b, path):
        if self.visited[a]:
            return
        path.append(a)
        self.visited[a] = True
 
        if a == b and not self.found:
            self.found = True # polku on löytynyt
            self.path = path[:] # otetaan polku muistiin
            print("TÄYDENNYSPOLKU LÖYTYI: ",path)
 
        for i in range(1, 2*self.n + 2):
            if self.residual_graph[a][i] > 0:
                self.dfs(i, b, path)
 
        path.pop()
 
    def calculate(self):
        a = 0 # lasketaan maksimivirtaus aina alkusolmusta...
        b = 2*self.n + 1 # loppusolmuun
 
        self.max_flow = 0
        self.residual_graph = deepcopy(self.graph) # luodaan deepcopy varsinaisesta verkosta, jotta se säilyy muuttumattomana

        while True:
            self.found = False
            path = [] # täydennyspolku = augmenting path
            self.visited = [False] * (2*self.n + 2)
 
            self.dfs(a,b,path)
 
            if not self.found:
                break
            
            min_weight = 10**9
 
            # etsitään minimipaino
            for i in range(len(self.path)-1):
                # tulostetaan ensin täydennyspolun kaaret ja niiden painot
                # print("kaari: a, b, paino:", self.path[i], self.path[i+1], self.residual_graph[self.path[i]][self.path[i+1]])
 
                # päivitetään minimipaino
                min_weight = min(min_weight, self.residual_graph[self.path[i]][self.path[i+1]])
 
            # muutetaan kaaret minimipainon mukaan (virtauskaaret vähentyvät, vastakkaiset lisääntyvät)
            for i in range(len(self.path)-1):
                self.residual_graph[self.path[i]][self.path[i+1]] -= min_weight
                self.residual_graph[self.path[i+1]][self.path[i]] += min_weight
 
            self.max_flow += min_weight
 
        return self.max_flow

if __name__ == "__main__":
    b = Ball(4)
    # print(b.calculate()) # 0
    b.add_pair(1,2)
    # print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2

    # b = Ball(5)
    # print(b.calculate()) # 0
    # b.add_pair(5,5)
    # print(b.calculate()) # 1
    # b.add_pair(3,4)
    # print(b.calculate()) # 2
    # print(b.calculate()) # 2
    # print(b.calculate()) # 2
    # b.add_pair(1,3)
    # b.add_pair(4,2)
    # print(b.calculate()) # 4
    # b.add_pair(5,3)
    # b.add_pair(5,1)
    # b.add_pair(1,4)
    # b.add_pair(1,2)
    # b.add_pair(1,3)
    # print(b.calculate()) # 4

    # print(b.calculate())
    # b.add_pair(4,5)
    # print(b.calculate())
    # b.add_pair(2,5)
    # b.add_pair(5,5)
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(3,1)
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(5,3)
    # print(b.calculate())
    # b.add_pair(3,5)

    # b = Ball(5)
    # b.add_pair(4,3)
    # print(b.calculate())
    # b.add_pair(4,1)
    # print(b.calculate())
    # b.add_pair(2,2)
    # print(b.calculate())
    # b.add_pair(5,3)
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(1,1)
    # print(b.calculate())
    # b.add_pair(4,3)
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(2,4)
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(2,4)
    # b.add_pair(2,3)
    # print(b.calculate())
    # print(b.calculate())
    # b.add_pair(5,1)
    # b.add_pair(5,5)
    # print(b.calculate())
    # b.add_pair(1,2)
    # print(b.calculate())
    # b.add_pair(4,1)