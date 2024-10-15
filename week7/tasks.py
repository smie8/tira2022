# Tehtäväsi on toteuttaa tietorakenne, joka pitää yllä tehokkaasti työlistaa. 
# Listalle voi lisätä uuden tehtävän, jolla on tietty nimi ja prioriteetti, 
# sekä listalta voi hakea käsittelyyn suurimman prioriteetin tehtävän.

# Voit olettaa, että työtehtävän nimi muodostuu merkeistä a–z ja 0–9 ja 
# prioriteetti on kokonaisluku välillä 0…10^9.

# Toteuta tiedostoon tasks.py luokka Tasks, jossa on seuraavat funktiot:
# - add: lisää listalle työtehtävän, jolla on tietty nimi ja prioriteetti
# - next: poistaa listalta korkeimman prioriteetin työtehtävän ja antaa 
# sen nimen (jos vaihtoehtoja on monta, valitaan aakkosjärjestyksessä ensimmäinen)

# Kummankin funktion tulee toimia tehokkaasti.

from heapq import heappush, heappop

class Tasks:
    def __init__(self):
        self.heap = []

    def add(self, name, priority):
        heappush(self.heap, (-priority, name))

    def next(self):
        next = heappop(self.heap)

        return next[1]

if __name__ == "__main__":
    t = Tasks()
    t.add("siivous",10)
    t.add("ulkoilu",50)
    t.add("opiskelu",50)
    print(t.next()) # opiskelu
    t.add("treffit",100)
    print(t.next()) # treffit
    print(t.next()) # ulkoilu