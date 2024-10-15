def dfs(r, y, x):
    global roomCount, seen
    if r[y][x] == '#' or seen[y][x]:
        return

    # if seen[y][x] == False:
    seen[y][x] = True
        # roomCount += 1

    dfs(r, y-1, x)
    dfs(r, y+1, x)
    dfs(r, y, x-1)
    dfs(r, y, x+1)

def count(r):
    n = len(r)
    m = len(r[0])

    global roomCount, seen
    roomCount = 0
    seen = [[False]*(m) for i in range(n)]

    for i in range(n):
        s = ""
        for j in range(m):
            if r[i][j] == '.' and seen[i][j] == False:
                dfs(r, i, j)
                roomCount += 1

    # for i in range(n):
    #     s = ""
    #     for j in range(m):
    #         if r[i][j] == '.':
    #             s += '0'
    #         else:
    #             s += '1'
    #     print(s)

            # if r[i][j] == '.' and seen[i][j] == False:
            #     roomCount += 1
                # dfs(r, i, j)

    return roomCount

    # go through items
    # when floor and not visited
        # execute dfs and mark adjacent floor visited
        # increase global variable roomCount
    # return room count
    

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3