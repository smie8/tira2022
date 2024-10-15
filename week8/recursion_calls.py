def calls(n):
    if n <= 2:
        return 1
    return calls(n-1) + calls(n-2) + calls(n-3) + 1

print(calls(10)) # 289