t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = list()
    mid = []
    min_el = 999999
    for el in a:
        if len(mid) == min_el:
            result.append(mid)
            mid = []

        if not mid:
            mid.append(el)
            min_el = el
            continue

        if min_el < el:
            mid.append(el)
        elif min_el >= el > len(mid):
            mid.append(el)
            min_el = el
        elif min_el >= el <= len(mid):
            result.append(mid)
            mid = [el]
            min_el = el
    result.append(mid)
    print(len(result))
    for el in result:
        print(len(el), end=' ')









