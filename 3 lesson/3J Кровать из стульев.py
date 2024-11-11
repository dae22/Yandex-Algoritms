n, H = map(int, input().split())
visota = list(map(int, input().split()))
shirina = list(map(int, input().split()))
chairs = sorted(zip(visota, shirina), key=lambda x: x[0])
pref = [0] * n
for i in range(1, n):
    pref[i] = chairs[i][0] - chairs[i-1][0]

dis_m = 10**10
mid = []
dis = []
w, r = 0, 0
if max(shirina) >= H:
    print(0)
    exit()
for i in range(n):
    while len(dis) and i >= dis[0][0]:
        dis.pop(0)
    while w < H and r < n:
        mid.append(chairs[r])
        if not len(dis):
            dis.append([r, pref[r]])
        elif dis[-1][1] >= pref[r]:
            dis.append([r, pref[r]])
        else:
            while len(dis) and dis[-1][1] < pref[r]:
                dis.pop(-1)
            dis.append([r, pref[r]])
        w += chairs[r][1]
        r += 1
    if w >= H:
        if r == i+1:
            dis_c = 0
        else:
            dis_c = dis[0][1]
        dis_m = min(dis_m, dis_c)
    w -= mid[0][1]
    mid.pop(0)
print(dis_m)
