# Tehtäväsi on etsiä listasta pisin alijono, 
# jossa jokaisen kahden vierekkäisen luvun ero on enintään 1.

def find(arr):
    longests = [0] * len(arr)
    longest = 1

    for k in range(len(arr)):
        longests[k] = 1
        for x in range(k):
            if abs(arr[x] - arr[k]) <= 1 and longests[x] + 1 > longests[k]:
                longests[k] = longests[x] + 1
                longest = longests[k] if longests[k] > longest else longest

    return longest

if __name__ == "__main__":
    print(find([1,2,3,4,5])) # 5
    print(find([5,5,5,5,5])) # 5
    print(find([5,2,3,8,2,4,1])) # 4
    print(find([1,3,5,7,9])) # 1