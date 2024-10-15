def func(n):
    if n <= 2:
        return n
    return func(n-1) + func(n-2) + func(n-3)

if __name__ == "__main__":
    print(func(230))