# Pelaat peliä, jossa on n tasoa. Olet aluksi tasolla 0 ja sinun tulee päästä tasolle n. 
# Joka askeleella voit hypätä a tai b tasoa ylemmäs. Monellako tavalla voit läpäistä pelin?

def count(n,a,b):
    jumps = [0] * (n + 1)

    # vain yksi hyppy näille tasoille
    jumps[0] = 1
    jumps[a] = 1
    jumps[b] = 1

    for i in range(1, n + 1):
        if i >= a:
            jumps[i] = jumps[i - a]
        if i >= b:
            jumps[i] += jumps[i - b]

    return jumps[-1]

if __name__ == "__main__":
    print(count(3,1,2)) # 3
    print(count(3,1,3)) # 2
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456