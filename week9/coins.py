def count(arr):
    n = len(arr) # count of coins
    s = 0 # max sum of coins
    for x in arr:
        s += x

    sums = [False] * (s + n)
    sums[0] = True

    for i in range(n):
        for j in range(s):
            j = s - j - 1
            if sums[j]:
                sums[j + arr[i]] = True

    count = 0
    for i in range(len(sums)):
        if sums[i] and i > 0:
            count += 1
            
    return count

if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91