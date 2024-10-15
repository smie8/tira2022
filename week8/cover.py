def count(n, m, k):
    if k == 1:
        return 1
    # if k > (a tai b): k = a tai b

if __name__ == "__main__":
    print(count(2,2,4)) # 8
    print(count(2,3,3)) # 13
    print(count(4,4,1)) # 1
    print(count(4,3,10)) # 3146
    print(count(4,4,16)) # 70878

    # 1,2,2 = 2
    # 2,1,2 = 2
    # 2,1,3 = 2

    # 2,2,2 = 3
    # 2,2,3 = 3
    # 2,3,2

    # 2,3,3 = 13
