n = int(input())
a, b = map(int, input().split())

s1, s2, s3, s4 = [], [], [], []
macros = {1: 's1.append(r)', 2: 's2.append(r)', 3: 's3.append(r)', 4: 's4.append(r)'}
for i in range(n):
    r = list(map(int, input().split()))
    r.append(i)
    exec(macros[r[0]])

print(s1, s2, s3, s4)
