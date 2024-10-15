import time
import functools

# "memoize"-tapa
def memoize(k):
    memo = {}
    def partner(l):
        if l not in memo:
            memo[l] = k(l)
        return memo[l]
    return partner

@memoize
def func(n):
    if n <= 2:
        return n
    return func(n-1) + func(n-2) + func(n-3)

# toinen tapa
memory = {}
def func2(n):
    if n <= 2:
        return n

    if n in memory:
        return memory[n]

    memory[n] = func(n-1) + func(n-2) + func(n-3)
    
    return func(n-1) + func(n-2) + func(n-3)

if __name__ == "__main__":
    start1 = time.time()
    print(func(30))
    end1 = time.time()
    print('time: ', end1 - start1)

    start2 = time.time()
    print(func(30))
    end2 = time.time()
    print('time: ', end2 - start2)

    print(func2(30))