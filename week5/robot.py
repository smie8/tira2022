# Robotti on alussa ruudussa (0,0). Tämän jälkeen robotti liikkuu annetun liikesarjan 
# mukaisesti askeleen kerrallaan. Liikesarja muodostuu merkeistä 
# U (up), D (down), L (left) ja R (right). 
# Monessako eri ruudussa robotti käy yhteensä?

# Voit olettaa, että liikesarjassa on enintään 10^5 komentoa.

# Toteuta tiedostoon robot.py funktio count, jolle annetaan robotin liikesarja ja 
# joka ilmoittaa eri ruutujen määrän.

def count(s):
    coordinates = {}
    coordinates["0,0"] = 1
    x = 0
    y = 0

    for i in range(len(s)):
        
        command = s[i]
        if command == "L":
            x -= 1
        elif command == "R":
            x += 1
        elif command == "U":
            y += 1
        elif command == "D":
            y -= 1

        coordinatesStr = str(x) + "," + str(y)
        if coordinatesStr in coordinates.keys():
            coordinates[coordinatesStr] += 1
        else:
            coordinates[coordinatesStr] = 0
        
    return len(coordinates.keys())

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2