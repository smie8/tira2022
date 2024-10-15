# Seuraava pseudokoodi esittää rekursiivisen funktion check, joka tarkastaa, onko positiivinen luku n kakkosen potenssi.
#
# function check(n)
#     if n == 1
#         return true
#     if n%2 == 0
#         return check(n/2)
#     return false
#
# Toteuta pseudokoodia vastaava funktio Pythonilla.

def check(n):
    if n == 1:
        return True
    if n%2 == 0:
        return check(n/2)
    return False

if __name__ == "__main__":
    print(check(1)) # True
    print(check(8)) # True
    print(check(12)) # False
    print(check(1099511627776)) # True
    print(check(123456789)) # False