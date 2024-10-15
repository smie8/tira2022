class Cycles:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def add_edge(self, a, b):
        self.edges[a-1].append(b-1)

    def check(self):
        visited = [False for _ in range(self.n)]
        rec_stack = [False for _ in range(self.n)]

        def dfs(node):
            if not visited[node]:
                visited[node] = True
                rec_stack[node] = True

            for neighbor in self.edges[node]:
                if not visited[neighbor] and dfs(neighbor):
                    return True
                elif rec_stack[neighbor]:
                    return True
            
            rec_stack[node] = False
            return False

        for node in range(self.n):
            if dfs(node):
                return True
        
        return False

if __name__ == "__main__":
    c = Cycles(5)
    print(c.check())
    c.add_edge(5,5)
    print(c.check())
    c.add_edge(3,4)
    print(c.check())
    print(c.check())
    print(c.check())
    c.add_edge(1,3)
    c.add_edge(4,2)
    print(c.check())

    print('----')

    c = Cycles(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(1,3)
    c.add_edge(3,4)
    print(c.check()) # False
    c.add_edge(4,2)
    print(c.check()) # True