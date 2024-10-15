class Airports2:
    def __init__(self,n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]

    def add_link(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def check(self):

        airports = set()

        def dfs(node, airports):
            airports.add(node)

            for y in self.graph[node]:
                dfs(y, airports)

            if len(airports) != n:
                return False
        
        for i in range(1, self.n + 1):
            dfs(i, airports)
            airports.clear()
        return True

class Airports3:
    def __init__(self, num_airports):
        self.num_airports = num_airports
        self.graph = [[] for _ in range(num_airports + 1)]
        self.visited = [False] * (num_airports + 1)

    def add_link(self, a, b):
        self.graph[a].append(b)

    def check(self):
        # We check if every airport can reach every other airport
        # by starting a DFS from each airport and marking all the
        # airports that can be reached from that airport.
        for i in range(1, self.num_airports + 1):
            self.visited = [False] * (self.num_airports + 1)
            self.dfs(i)

            # If there is an airport that cannot be reached
            # from the current airport, then return False.
            if False in self.visited:
                return False

        # If every airport can reach every other airport, then return True.
        return True

    def dfs(self, node):
        # Mark the current node as visited.
        self.visited[node] = True

        # Recursively visit all the neighbors of the current node.
        for neighbor in self.graph[node]:
            if not self.visited[neighbor]:
                self.dfs(neighbor)

class Airports:
    def __init__(self, num_airports):
        self.num_airports = num_airports
        self.graph = [[] for _ in range(num_airports + 1)]
        self.visited = [False] * (num_airports + 1)

    def add_link(self, a, b):
        self.graph[a].append(b)

    def check(self):
        # We check if every airport can reach every other airport
        # by starting a DFS from each airport and marking all the
        # airports that can be reached from that airport.
        for i in range(1, self.num_airports + 1):
            self.visited = [False] * (self.num_airports + 1)
            self.dfs(i)

            # If there is an airport that cannot be reached
            # from the current airport, then return False.
            if False in self.visited:
                return False

        # If every airport can reach every other airport, then return True.
        return True

    def dfs(self, node):
        # Create a stack to store the nodes that need to be visited.
        stack = []
        stack.append(node)

        while stack:
            # Pop the top node from the stack.
            node = stack.pop()

            # Mark the current node as visited.
            self.visited[node] = True

            # Add all the unvisited neighbors of the current node to the stack.
            for neighbor in self.graph[node]:
                if not self.visited[neighbor]:
                    stack.append(neighbor)

if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1,2)
    a.add_link(2,3)
    a.add_link(1,3)
    a.add_link(4,5)
    print(a.check()) # False
    a.add_link(3,5)
    a.add_link(1,4)
    print(a.check()) # False
    a.add_link(5,1)
    print(a.check()) # True