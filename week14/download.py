from copy import deepcopy

class Download:
    def __init__(self,n):
        self.n = n
        self.graph = [[0] * (n + 1) for _ in range(n + 1)] # luo n+1-kokoisen listan jossa yksi alkio on n+1-kokoinen lista
        self.residual_graph = None
        self.found = False 
        self.visited = [False] * (self.n + 1) # luo n+1-kokoisen listan jossa yksi alkio on Boolen arvo
        self.max_flow = 0
        self.result = []

    def add_link(self,a,b,x):
        self.graph[a][b] += x

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
            if self.residual_graph[a][i] > 0:
                self.dfs(i, b, path)

        path.pop()

    def calculate(self,a,b):
        print("calculate(",a,",",b,")")

        self.max_flow = 0
        self.found = False
        self.residual_graph = deepcopy(self.graph) # luodaan deepcopy varsinaisesta verkosta, jotta se säilyy muuttumattomana

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
                print("kaari: a, b, paino:", self.result[i], self.result[i+1], self.residual_graph[self.result[i]][self.result[i+1]])

                # päivitetään minimipaino
                min_weight = min(min_weight, self.residual_graph[self.result[i]][self.result[i+1]])

            # muutetaan kaaret minimipainon mukaan (virtauskaaret vähentyvät, vastakkaiset lisääntyvät)
            for i in range(len(self.result)-1):
                self.residual_graph[self.result[i]][self.result[i+1]] -= min_weight
                self.residual_graph[self.result[i+1]][self.result[i]] += min_weight

            self.max_flow += min_weight

        return self.max_flow

if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1,4)) # 0
    print('')
    d.add_link(1,2,5)
    d.add_link(2,4,6)
    d.add_link(1,4,2)
    print(d.calculate(1,4)) # 7
    print('')
    d.add_link(1,3,4)
    d.add_link(3,2,2)
    print(d.calculate(1,4)) # 8
    print('')

    d = Download(5)
    print(d.calculate(3,4)) # 0
    d.add_link(5,3,6)
    print(d.calculate(5,4)) # 0
    print(d.calculate(4,5)) # 0
    print(d.calculate(5,1)) # 0
    d.add_link(5,4,9)
    d.add_link(1,2,10)
    print(d.calculate(3,1)) # 0
    print(d.calculate(2,4)) # 0
    print(d.calculate(5,4)) # 9
    d.add_link(5,2,9)
    print(d.calculate(1,5)) # 0
    d.add_link(3,5,2)
    d.add_link(1,3,2)
    d.add_link(5,4,9)
    print(d.calculate(5,4)) # 18
    print(d.calculate(2,3)) # 0
    print(d.calculate(1,3)) # 2
    print(d.calculate(3,2)) # 2
    print(d.calculate(5,4))
    print(d.calculate(4,5))
    d.add_link(4,3,9)
    print(d.calculate(4,5))
    print(d.calculate(2,4))
    print(d.calculate(4,5))
    d.add_link(5,1,6)
    d.add_link(3,5,3)
    d.add_link(4,5,2)
    print(d.calculate(3,4))
    d.add_link(5,3,3)

    # d2 = Download(5)
    # d2.add_link(1,3,4)
    # d2.add_link(1,2,3)
    # d2.add_link(2,4,8)
    # d2.add_link(3,4,2)
    # d2.add_link(4,5,3)
    # print(d2.calculate(1,5))
    # print('')