n, k = map(int, input().split())
works = sorted(map(int, input().split()))

max_ln = 0
right = 1
ln = 1
for left in range(n):
    while right < n and works[right] - works[left] <= k:
        ln += 1
        right += 1
    max_ln = max(max_ln, ln)
    ln -= 1
print(max_ln)
