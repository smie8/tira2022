import time

def recursion(n):
    if n <= 2:
        return n
    return recursion(n-1) + recursion(n-2) + recursion(n-3)

start = time.time()
print(recursion(30))
end = time.time()
print(end-start, ' seconds')