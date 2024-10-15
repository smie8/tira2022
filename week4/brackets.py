def balance(s):
    list = []
    count = []

    # count the stars
    stars = 0
    for i in range(len(s)):
        if s[i] == '*':
            stars += 1
            starIndex = i

    # laske montako ) on yksitähtisessä listassa * jälkeen 
    # ja break silloin looppi jos bracketCount - len(list) - rightBracketCount == 0:
    rightBracketCountAfterOnlyStar = 0
    if stars >= 1:
        list2 = []
        # start = s.find('*')
        start = starIndex
        for i in range(start, len(s)):
            if s[i] == '(':
                list2.append('(')
            if s[i] == ')':
                if len(list2) > 0:
                    list2.pop()
                else:
                    rightBracketCountAfterOnlyStar += 1

    # print('rightbracks', rightBracketCountAfterOnlyStar)

    for i in range(len(s)):        
        if s[i] == '(' and i == len(s) - 1:
            return None

        if s[i] == '(':
            list.append('(')

        if s[i] == ')':
            if len(list) == 0 and len(count) > 0 and i > len(s) - 2:
                count[-1] -= 1
                return count

            if len(list) == 0:
                return None
            list.pop()
        
        if s[i] == '*':
            bracketCount = 0

            if len(list) == 0:
                return None

            while list[-1] == '(':
                bracketCount += 1
                list.pop()

                if stars > 1 and len(count) < stars - 1:
                    break

                if len(list) == 0:
                    if rightBracketCountAfterOnlyStar > 0:
                        return None
                    break

                if len(list) == 1 and i < len(s) - 2 and (s[i+1] != '(' and s[i+2] != ')'):
                    break

                if rightBracketCountAfterOnlyStar > 0 and bracketCount - len(list) - rightBracketCountAfterOnlyStar == 0 and rightBracketCountAfterOnlyStar == len(list):
                    break

                # TODO: tarviiko tähän jonkin tsekkauksen että viimeinen tähti menossa (counter yms)
                if len(list) == rightBracketCountAfterOnlyStar:
                    break

            count.append(bracketCount)

    if len(list) > 0:
        return None

    return count

if __name__ == "__main__":
    print(balance("*(")) # None
    print(balance("(*")) # len 1
    print(balance("(())")) # []
    print(balance("(((((*")) # len 1
    print(balance("(((((*(")) # None
    print(balance("((((*(()*()*")) # len 3
    print(balance("((*))(((*")) # None
    print(balance("(((*)()")) # len 1
    print(balance("(((*())()")) # len 1
    print(balance("(((**()")) # len 2 
    print(balance("(((*((()*)")) # len 2 
    print(balance("(((()(*))(")) # None
    print(balance("(((*())()")) # len 1
    print(balance("(((((*(**))")) # len 3
    print(balance("(())(((((((*))))")) # len 1´
    print(balance("(((()(((())*)")) # len 1

    print(balance("((**)")) # None
