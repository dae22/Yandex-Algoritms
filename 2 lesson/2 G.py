n, k = map(int, input().split())
s = input()

d = dict()
l = r = mln = 0
g = 0

while r < n:
    if g <= k:
        d[s[r]] = d.get(s[r], 0) + 1
        if s[r] == 'b' and d.get('a', 0) > 0:
            g += d['a']
        r += 1
    else:
        while l < n and g > k:
            d[s[l]] -= 1
            if s[l] == 'a':
                g -= d['b']
            l += 1
    if g <= k:
        mln = max(mln, r-l)

print(mln)
