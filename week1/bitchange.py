# Bittijonossa on aluksi n bittiä ja jokainen bitti on 0. Sitten bittijonoa muutetaan k kertaa. 
# Joka muutoksessa bittijonoa käydään läpi vasemmalta oikealle. Jos bitti on 1, siitä tulee 0
# ja läpikäynti jatkuu. Jos taas bitti on 0, siitä tulee 1 ja läpikäynti päättyy. 
# Millainen bittijono on lopuksi?

# Voit olettaa, että n on välillä 1…20 ja k on välillä 0…1000. Lisäksi voit olettaa, 
# että k<2n eli joka muutoksessa bittijonossa on ainakin yksi bitti 0.

# Toteuta tiedostoon bitchange.py funktio create, joka palauttaa lopullisen bittijonon merkkijonona.

def create(n, k):
    bitsRaw = str(bin(k))
    bits = bitsRaw[2:len(bitsRaw)]
    bitsReversed = bits[::-1]
    zeros = str((n - len(bits)) * '0')

    return bitsReversed + zeros

if __name__ == "__main__":
    print(create(5, 0)) # 00000
    print(create(5, 1)) # 10000
    print(create(5, 2)) # 01000
    print(create(5, 3)) # 11000
    print(create(5, 4)) # 00100
    print(create(5, 31)) # 11111
    print(create(20, 947)) # 11001101110000000000