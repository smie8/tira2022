# Toteuta testi, jossa listaan lisätään ensin luvut 1,2,…,n yksi kerrallaan listan loppuun. 
# Tämän jälkeen listasta poistetaan n kertaa ensimmäinen alkio.

# Käytä testissä taulukkolistaa eli Pythonissa tavallista listaa [].

# Toteuta testi niin, että n=10^5. Mittaa kaksi aikaa: kauanko kestää lisätä luvut listalle 
# ja kauanko kestää poistaa ne listalta.

import time

list = []
start1 = time.time()

for i in range(1, 10000 + 1):
    list.append(i)

end1 = time.time()

print('adding numbers took ', end1 - start1, ' s')

start2 = time.time()

for i in range(1, 10000 + 1):
    list.pop(0)

end2 = time.time()

print('removing numbers took ', end2 - start1, ' s')