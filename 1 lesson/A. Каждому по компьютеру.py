n, m = map(int, input().split())
students = sorted(enumerate(map(int, input().split()), 1), key=lambda x: x[1])
classes = sorted(enumerate(map(int, input().split()), 1), key=lambda x: x[1])

result = [0] * n
count = 0
cl = 0
for i, size in students:
    while True:
        if cl <= m - 1 and size + 1 <= classes[cl][1]:
            result[i-1] = classes[cl][0]
            count += 1
            cl += 1
            break
        elif cl > m - 1:
            break
        else:
            cl += 1

print(count)
print(*result)
