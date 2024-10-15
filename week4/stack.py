# Tehtäväsi on toteuttaa oma tehokas pino-tietorakenne, joka tarjoaa seuraavat toiminnot:
# - Lisää luku pinon päälle
# - Palauta ja poista luku pinon päältä
# - Kasvata pinon k päällimmäisen luvun arvoa yhdellä
# Tietorakenteen jokaisen operaation tulee olla O(1)-aikainen. Voit olettaa, että 
# jokainen alkio on kokonaisluku väliltä 1…10^9.

# Toteuta tiedostoon stack.py luokka Stack seuraavan mallin mukaisesti.

from collections import deque

# idea: älä oikeasti kasvata arvoja, vaan pidä kirjaa kasvatusoperaatioista

class Stack:
    def __init__(self):
        self.s = deque()
        self.increases = [(0, 0)]
        # koeta keksiä miten saat increaset tallennettua pelkkänä taulukkona muutoksista

        # Ajattele konseptia "ensimmäisiin 10 tehdään operaatio X" tältä kannalta: 
        # "ensimmäiseen 0 ja kaikkiin sen jälkeen tehdään operaatio X", 
        # ja "kaikkiin indeksistä 10 alkaen tehdään operaatio –X"

        # Tehtävä muuttuu paljon intuitiivisemmaksi, jos kuvittelet, 
        # että pushit, popit ja increaset tehdäänkin alusta laskien 
        # eikä lopusta (eli esim. 10 ensimmäistä eikä 10 viimeistä).

    def push(self, x):
        self.s.append(x)
        self.increases.append(deque())
        # kasvata increase-taulukkoa myös

    def pop(self):

        return self.s.pop()
        # pienennä increase-taulukkoa myös

    def increase(self, k):
        self.increases

if __name__ == "__main__":
    s = Stack()
    s.push(7)
    s.push(10)
    print(s.pop()) # 10
    print(s.pop()) # 7
    s.push(4)
    s.push(7)
    s.increase(2)
    s.increase(1)
    print(s.pop()) # 9
    print(s.pop()) # 5


    s = Stack()
    s.push(7)
    print(s.pop()) # 7
    s.push(6)
    s.increase(1)
    s.push(5)
    s.push(1)
    s.increase(3)
    print(s.pop()) # 2
    s.increase(1)
    print(s.pop()) # 7

    s = Stack()
    s.push(9)
    s.push(6)
    s.push(9)
    s.push(5)
    s.increase(1)
    s.push(3)
    print(s.pop()) # 3
    print(s.pop()) # 6
    s.increase(1)
    print(s.pop()) # 10

    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.increase(2)
    print(s.pop()) # 4
    s.push(1)
    s.increase(2)
    print(s.pop()) # 2
    print(s.pop()) # 4
    print(s.pop()) # 1

    s = Stack()
    s.push(9)
    s.push(6)
    s.push(10)
    s.push(3)
    s.increase(4)
    s.push(6)
    s.increase(4)
    s.push(4)
    s.push(6)
    print(s.pop()) # 6

    s = Stack()
    for i in range(5*10**4):
        s.push(i+1)
    for i in range(5*10**4 - 1):
        s.increase(5*10**4)
    print(s.pop())

    s = Stack()
    for i in range(14000):
        for j in range(3):
            s.push(i*i + 1)
        s.increase(i+1)
        print(s.pop())
    for i in range(28000):
        print(s.pop())


# class Stack:
#     def __init__(self):
#         self.s = deque()
#         self.increases = [] # mistä mihin

#     def push(self, x):
#         self.s.append(x)

#     def pop(self):
#         increase = 0
#         for i in range(len(self.increases)):
#             if self.increases[len(self.increases)-1-i][1] == len(self.s) and self.increases[len(self.increases)-1-i][1] >= self.increases[len(self.increases)-1-i][0]:
#                 self.increases[len(self.increases)-1-i][1] -= 1
#                 increase += 1

#         return self.s.pop() + increase

#     def increase(self, k):
#         self.increases.append([len(self.s)-k+1, len(self.s)]) # mistä koosta mihin


# # TODO: tämä ratkaisu on nopein
# class Stack:
#     def __init__(self):
#         self.s = deque()
#         self.increases = []

#     def push(self, x):
#         self.s.append(x)
#         self.increases.append(0)

#     def pop(self):
#         increase = self.increases[len(self.s)-1]
#         self.increases.pop()

#         return self.s.pop() + increase

#     def increase(self, k):
#         for i in range(k):
#             self.increases.append([len(self.s)-k+1, len(self.s)])

# class Stack:
#     def __init__(self):
#         self.s = deque()
#         self.increases = []

#     def push(self, x):
#         self.s.append(x)

#     def pop(self):
#         increase = 0
#         for i in range(len(self.increases)):
#             if self.increases[i][0] <= len(self.s) and self.increases[i][1] == len(self.s):
#                 # vähennetään "mihin" arvoa kun increasen viimeisin ulottuva arvo poistetaan
#                 self.increases[i][1] -= 1
#                 increase += 1
                
#         return self.s.pop() + increase

#     def increase(self, k):
#         # tallennetaan mistä koosta mihin kyseinen increase on voimassa
#         self.increases.append([len(self.s)-k+1, len(self.s)])