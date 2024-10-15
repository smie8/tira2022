# Maksimikekoon lisätään järjestyksessä luvut 1,2,…,n. 
# Kuinka monta kertaa kahden eri alkion paikkaa vaihdetaan 
# keskenään keossa kyseisen prosessin aikana? 
# Voit olettaa, että n on korkeintaan 10^9.

# Esimerkiksi kun n=4, vaihdot ovat järjestyksessä 
# 1↔2, 2↔3, 1↔4 ja 3↔4, joten vastaus on 4.
import math

def count(n):
    swapCount = 0
    height = math.ceil(math.log2(n + 1))
    numsLeft = n

    level = 1
    numsInLevel = 1
    num = 1

    while numsLeft > 0:
        if level == height:
            swapCount += numsLeft * math.floor(math.log2(num))
        else:
            swapCount += numsInLevel * math.floor(math.log2(num))

        numsLeft -= numsInLevel

        numsInLevel *= 2
        num += numsInLevel
        level += 1
    return swapCount

if __name__ == "__main__":
    print(count(4)) # 4
    print(count(7)) # 10
    print(count(123)) # 618
    print(count(999999999)) # 27926258178