# Toteuta kurssikirjan luvussa 2.1.4 kuvattu tehokkuustesti omalla koneellasi. 
# Toteuta algoritmit Pythonilla ja mittaa niiden suoritusaika, kun n=10^5. 
# Käytä testissä satunnaista syötettä, jossa jokaisessa kohdassa merkin 0 ja 1 
# todennäköisyys tulla valituksi on yhtä suuri.
import time

chars = '01'*10000

def counter(chars):
    counter = 0
    for i in range(len(chars)-1):
        for j in range(i+1, len(chars)-1):
            if chars[i] == '0' and chars[j] == '1':
                counter += 1
    print(counter)

def fasterCounter(chars):
    counter = 0
    zeros = 0
    for i in range(len(chars)-1):
        if chars[i] == '0':
            zeros += 1
        else:
            counter += zeros
    print(counter)


# O(n^2):
start1 = time.time()
counter(chars)
end1 = time.time()

print('time lapsed for O(n^2): ', end1-start1, ' s')

# O(n):
start2 = time.time()
fasterCounter(chars)
end2 = time.time()

print('time lapsed for O(n): ', end2-start2, ' s')


