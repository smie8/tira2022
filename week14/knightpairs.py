def count(r):
    pairs = make_pairs(r)
    return len(pairs)

def can_attack(r, row1, col1, row2, col2):
    # Tarkistetaan, että ratsut ovat sallitulla etäisyydellä toisistaan
    row_distance = abs(row1 - row2)
    col_distance = abs(col1 - col2)
    if (row_distance, col_distance) != (2, 1):
        return False

    # Tarkistetaan, että toisen ratsun välittömässä läheisyydessä ei ole muita ratsuja
    for i in [-1, 1]:
        for j in [-2, 2]:
            # Tarkistetaan, että tarkistettava ruutu on laudalla
            if not (0 <= row1 + i < len(r) and 0 <= col1 + j < len(r[0])):
                continue
            # Tarkistetaan, että ruudussa ei ole ratsua
            if r[row1 + i][col1 + j] == "*":
                return False

    return True

def make_pairs(r):
    pairs = []
    seen = set()
    for row1, row in enumerate(r):
        for col1, square in enumerate(row):
            if square == "*":
                if (row1, col1) in seen:
                    continue
                for row2, other_row in enumerate(r):
                    for col2, other_square in enumerate(other_row):
                        if other_square == "*" and (row1, col1) != (row2, col2):
                            if can_attack(r, row1, col1, row2, col2):
                                pairs.append(((row1, col1), (row2, col2)))
                                seen.add((row1, col1))
                                seen.add((row2, col2))
    return pairs

if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(count(r)) # 3