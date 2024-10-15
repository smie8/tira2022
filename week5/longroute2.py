def count(s,k):
    print('')
    coordinatesDict = {}
    coordinatesDict["0,0"] = 1
    x = 0
    y = 0

    newPointsThisRoundSet = set()
    newPointsThisRoundSet.add("0,0")

    newPointsThisRound = 0
    newPointsPreviousRound = 0

    constantChanges = 0
    cumulativeNewPointsBeforeConstantChanges = 0
    iterationsBeforeConstantChange = 0

    # iterate enough (at most 100 times) so we get the constant changes
    for j in range(1, 101):
        # set previous round points
        newPointsPreviousRound = newPointsThisRound

        # go through movement and save coordinates
        for i in range(len(s)):
            if s[i] == "L":
                x -= 1
            elif s[i] == "R":
                x += 1
            elif s[i] == "U":
                y += 1
            elif s[i] == "D":
                y -= 1

            point = str(x) + "," + str(y)

            if point in coordinatesDict.keys():
                coordinatesDict[point] += 1
            else:
                # add new point to dict
                coordinatesDict[point] = 1  
                # save new point to counted
                newPointsThisRoundSet.add(point)
            
        newPointsThisRound = len(newPointsThisRoundSet)

        cumulativeNewPointsBeforeConstantChanges += newPointsThisRound

        # number of constant changes is found
        if newPointsThisRound == newPointsPreviousRound:
            constantChanges = newPointsThisRound
            break
        
        # clear set of new points because it's end of the iteration
        newPointsThisRoundSet.clear()

        iterationsBeforeConstantChange += 1

    print('cumulativeNewPointsBeforeConstantChanges',cumulativeNewPointsBeforeConstantChanges)
    print('constantChanges', constantChanges)
    print('iterationsBeforeConstantChange', iterationsBeforeConstantChange)

    # return cumulative changes + (constant changes * iterations left)
    return cumulativeNewPointsBeforeConstantChanges + ((k - iterationsBeforeConstantChange - 1) * constantChanges)


if __name__ == "__main__":
    print(count("UR", 100)) # 201
    print(count("UD", 100)) # 2
    print(count("UURRDDL", 500)) # 1506
    print(count("L", 10**9)) # 1000000001
    print(count("DLUR", 10**9)) # 4
    print(count("LDLRLLRDLU", 9)) # 55
    print(count("RRRLDDRDRDLRDDDLLLRLULUDUDUUULURRLLRRDURDLURLURLUU", 27296520)) # 327558266
    print(count("UURRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRDDLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL", 1000000000)) # 3000000144