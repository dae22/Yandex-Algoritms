n, H = map(int, input().split())
chairs = sorted(zip(map(int, input().split()), map(int, input().split())), key=lambda x: x[0])
pref = [0] * n
for i in range(1, n):
    pref[i] = chairs[i][0] - chairs[i-1][0]

dis_m = 10000000000
mid = []
dis = []
w, r, ld = 0, 0, 0
for i in range(n):
    while ld > 0 and i >= dis[0][0]:
        dis.pop(0)
        ld -= 1
    while w < H and r < n:
        mid.append(chairs[r][1])
        if ld == 0:
            dis.append([r, pref[r]])
            ld += 1
        elif dis[-1][1] >= pref[r]:
            dis.append([r, pref[r]])
            ld += 1
        else:
            while ld > 0 and dis[-1][1] < pref[r]:
                dis.pop(-1)
                ld -= 1
            dis.append([r, pref[r]])
            ld += 1
        w += chairs[r][1]
        r += 1
    if w >= H:
        if r == i+1:
            dis_c = 0
        else:
            dis_c = dis[0][1]
        dis_m = min(dis_m, dis_c)
    w -= mid[0]
    mid.pop(0)
print(dis_m)
