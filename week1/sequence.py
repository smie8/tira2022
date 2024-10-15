# Lukujonon jokainen alkio on pienin positiivinen kokonaisluku, 
# jota ei ole vielä esiintynyt lukujonossa ja jossa on yksi tai useampi toistuva numero.

# Lukujono alkaa näin:
# 11,22,33,44,55,66,77,88,99,100,101,110,111,112,113,114,…

# Tehtäväsi on etsiä lukujonon kohdassa n oleva luku. Voit olettaa, että n on enintään 1000.

# Toteuta tiedostoon sequence.py funktio generate, joka palauttaa halutun lukujonon alkion.

def generate(n):
    validNumberCount = 0
    number = 0

    while True:
        if (atLeastTwoSameDigits(number)):
            validNumberCount += 1

        if validNumberCount == n:
            break
        
        number += 1

    return number

def atLeastTwoSameDigits(number):
    numbers = {}
    strNumber = str(number)

    # laita luvun numerot lukumäärineen dict-tietorakenteeseen
    for i in range(len(strNumber)):
        char = strNumber[i]
        if (numbers.get(char)):
            numbers[char] = numbers.get(char) + 1
        else:
            numbers[char] = 1

    # tarkista löytyykö luvusta vähintään kaksi samaa numeroa
    atLeastTwoNumbers = False
    for key in numbers:
        if numbers.get(key) >= 2:
            atLeastTwoNumbers = True
    return atLeastTwoNumbers

if __name__ == "__main__":
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505