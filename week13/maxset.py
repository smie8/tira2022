class MaxSet:
    def __init__(self,n):
        self.link = list(range(n + 1))
        self.size = [1] * (n + 1)
        self.n = n
        self.max = 1

    def find(self,x):
        while self.link[x] != x:
            x = self.link[x]
        return x

    def merge(self,a,b ):
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
        self.max = max(self.max, self.size[a], self.size[b])
    
    def get_max(self):
        return self.max

if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max())  # 1
    m.merge(1, 2)
    m.merge(3, 4)
    m.merge(3, 5)
    print(m.get_max())  # 3
    m.merge(1, 5)
    print(m.get_max())  # 5

    # m = MaxSet(100000)
    # m.merge(99999,100000)
    # print(m.get_max())
    # m.merge(99998,100000)
    # print(m.get_max())
    # m.merge(99997,100000)
    # print(m.get_max())
    # m.merge(99996,100000)
    # print(m.get_max())
    # m.merge(99995,100000)
    # print(m.get_max())
    # m.merge(99994,100000)
    # print(m.get_max())
    # m.merge(99993,100000)
    # print(m.get_max())
    # m.merge(99992,100000)
    # print(m.get_max())
    # m.merge(99991,100000)
    # print(m.get_max())
    # m.merge(99990,100000)
    # print(m.get_max())
    # m.merge(99989,100000)
    # print(m.get_max())
    # m.merge(99988,100000)
    # print(m.get_max())
    # m.merge(99987,100000)
    # print(m.get_max())
    # m.merge(99986,100000)
    # print(m.get_max())
    # m.merge(99985,100000)
    # print(m.get_max())
    # m.merge(99984,100000)
    # print(m.get_max())
    # m.merge(99983,100000)
    # print(m.get_max())
    # m.merge(99982,100000)
    # print(m.get_max())
    # m.merge(99981,100000)
    # print(m.get_max())
    # m.merge(99980,100000)
    # print(m.get_max())
    # m.merge(99979,100000)
    # print(m.get_max())
    # m.merge(99978,100000)
    # print(m.get_max())
    # m.merge(99977,100000)
    # print(m.get_max())
    # m.merge(99976,100000)
    # print(m.get_max())
    # m.merge(99975,100000)
    # print(m.get_max())
    # m.merge(99974,100000)
    # print(m.get_max())
    # m.merge(99973,100000)
    # print(m.get_max())
    # m.merge(99972,100000)
    # print(m.get_max())
    # m.merge(99971,100000)
    # print(m.get_max())
    # m.merge(99970,100000)
    # print(m.get_max())
    # m.merge(99969,100000)
    # print(m.get_max())
    # m.merge(99968,100000)
    # print(m.get_max())
    # m.merge(99967,100000)
    # print(m.get_max())
    # m.merge(99966,100000)
    # print(m.get_max())
    # m.merge(99965,100000)
    # print(m.get_max())
    # m.merge(99964,100000)
    # print(m.get_max())
    # m.merge(99963,100000)
    # print(m.get_max())
    # m.merge(99962,100000)
    # print(m.get_max())
    # m.merge(99961,100000)
    # print(m.get_max())
    # m.merge(99960,100000)
    # print(m.get_max())
    # m.merge(99959,100000)
    # print(m.get_max())
    # m.merge(99958,100000)
    # print(m.get_max())
    # m.merge(99957,100000)
    # print(m.get_max())
    # m.merge(99956,100000)
    # print(m.get_max())
    # m.merge(99955,100000)
    # print(m.get_max())
    # m.merge(99954,100000)
    # print(m.get_max())
    # m.merge(99953,100000)
    # print(m.get_max())
    # m.merge(99952,100000)
    # print(m.get_max())
    # m.merge(99951,100000)
    # print(m.get_max())
    # m.merge(99950,100000)
    # print(m.get_max())