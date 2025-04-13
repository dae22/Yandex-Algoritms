n = int(input())
a, b = map(int, input().split())
c, d = [x for x in range(1,5) if x not in (a,b)]
rover = []
for i in range(n):
    x, y = map(int, input().split())
    rover.append([x, y, i])
rover.sort(key=lambda x: x[1])

queue = [None] * n
stack = {1: [], 2: [], 3: [], 4: []}
t, i = 0, 0
while True:
    t += 1
    while i < n and rover[i][1] == t:
        stack[rover[i][0]].append(rover[i])
        i += 1
    if stack[a] and stack[b]:
        if a+2 == b or b+2 == a:
            queue[stack[a][0][2]] = t
            queue[stack[b][0][2]] = t
            stack[a].pop(0)
            stack[b].pop(0)
        elif a == b+1 or a+3 == b:
            queue[stack[b][0][2]] = t
            stack[b].pop(0)
        elif b == a+1 or b+3 == a:
            queue[stack[a][0][2]] = t
            stack[a].pop(0)
    elif stack[a] and not stack[b]:
        queue[stack[a][0][2]] = t
        stack[a].pop(0)
    elif stack[b] and not stack[a]:
        queue[stack[b][0][2]] = t
        stack[b].pop(0)
    elif stack[c] and stack[d]:
        if c+2 == d or d+2 == c:
            queue[stack[c][0][2]] = t
            queue[stack[d][0][2]] = t
            stack[c].pop(0)
            stack[d].pop(0)
        elif c == d+1 or c+3 == d:
            queue[stack[d][0][2]] = t
            stack[d].pop(0)
        elif d == c+1 or d+3 == c:
            queue[stack[c][0][2]] = t
            stack[c].pop(0)
    elif stack[c] and not stack[d]:
        queue[stack[c][0][2]] = t
        stack[c].pop(0)
    elif stack[d] and not stack[c]:
        queue[stack[d][0][2]] = t
        stack[d].pop(0)
    if not (None in queue):
        break

for el in queue:
    print(el)
