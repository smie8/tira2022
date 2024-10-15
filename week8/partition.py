# onko luvut mmahdollista jakaa kahteen ryhmään niin että summat ovat samat

# käy läpi osajoukot
# tarkista jokaisen osajoukon kohdalla, onko valittujen lukujen summa sama kuin valitsemattomien
# jos on, lisää listaan

def search(t, ab):
    global result
    if len(t) == len(ab):
        sum1 = 0
        sum2 = 0
        for i in range(len(t)):
            if ab[i] == 'A':
                sum1 += t[i]
            else:
                sum2 += t[i]
        if sum1 == sum2:
            result = True
    else:
        search(t, ab + 'A')
        search(t, ab + 'B')

def check(t):
    global result
    result = False
    search(t, '')
    return result

if __name__ == "__main__":
    print(check([3,4,5])) # False
    print(check([16,8,4,4])) # True
    print(check([9,4,8,7,6])) # True
    print(check([1,2,3,4,5,6])) # False
    print(check([1,2,3,4,5,6,7])) # True
    print(check([4,4,4,6,6])) # True