# Sinulle annetaan lukuja yksi kerrallaan. Tehtäväsi on kertoa jokaisen luvun kohdalla, 
# mikä on siihen mennessä annettujen lukujen mex-luku eli pienin puuttuva epänegatiivinen luku.

# Voit olettaa, että jokainen luku on kokonaisluku välillä 0…109 ja lukuja annetaan enintään 10^5.

# Toteuta tiedostoon mex.py luokka Mex, jonka funktio add lisää uuden luvun ja palauttaa 
# lisättyjen lukujen mex-luvun.

class Mex:
    def __init__(self):
        # TODO
        self.arr = set()
        self.min = 0

    def add(self, x):
        # TODO
        self.arr.add(x)
        i = self.min
        while True:
            if i not in self.arr:
                self.min = i
                break
            else:
                i += 1

        return self.min

if __name__ == "__main__":
    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6