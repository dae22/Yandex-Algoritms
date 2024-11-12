n = int(input())
a, b = map(int, input().split())
b, c = [x for x in range(1,5) if x not in (a,b)]
rover = []
for i in range(n):
    x, y = map(int, input().split())
    rover.append([x, y, i])
rover.sort(key=lambda x: x[1])

queue = [''] * n
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
        elif a == b+1:
            queue[stack[b][0][2]] = t
        elif b == a+1:
            queue[stack[a][0][2]] = t
    elif stack[a] and not stack[b]:
        queue[stack[a][0][2]] = t
    elif stack[b] and not stack[a]:
        queue[stack[b][0][2]] = t

    if i == n: break

print(rover)
print(stack)
