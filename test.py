def longest_way(street):
    max_way = -1
    r = 0
    for l in range(len(street)):
        while r < len(street) and street[r] != 1:
            r += 1

