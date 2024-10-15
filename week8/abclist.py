def create(n): 
    if n == 1:
        return ["A", "B", "C"]
    else:
        old = create(n-1)
        new = []
        for s in old:
            new.append(s+"A")
            new.append(s+"B")
            new.append(s+"C")

        return new

if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(len(create(5))) # 243