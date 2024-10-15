# Sinulle annetaan lukuja yksi kerrallaan. Tehtäväsi on kertoa jokaisen luvun kohdalla, 
# mikä on siihen mennessä annettujen lukujen moodi (eli yleisin luku). 
# Jos moodeja on useita, niistä valitaan pienin mahdollinen.

# Voit olettaa, että jokainen luku on kokonaisluku välillä 1…109 ja 
# lukuja annetaan enintään 10^5.

# Toteuta tiedostoon mode.py luokka Mode, jonka funktio add lisää uuden luvun ja 
# palauttaa lisättyjen lukujen moodin.

class Mode:
    def __init__(self):
        self.nums = {}
        self.mode = [-1, 0]

    def add(self, x):
        if x in self.nums.keys():
            self.nums[x] += 1
        else:
            self.nums[x] = 1

        if self.mode[1] < self.nums[x] or self.mode[0] == -1:
            self.mode = [x, self.nums[x]]

        if self.mode[1] == self.nums[x] and x < self.mode[0]:
            self.mode = [x, self.nums[x]]

        return self.mode[0]

if __name__ == "__main__":
    m = Mode()
    print(m.add(1)) # 1
    print(m.add(2)) # 1
    print(m.add(2)) # 2
    print(m.add(1)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 1
    print(m.add(3)) # 3