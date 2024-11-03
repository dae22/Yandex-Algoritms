from collections import Counter

# если 1 - то полезный, если 0 - то интересный

n = int(input())
interes = list(map(int, input().split()))
polza = list(map(int, input().split()))
nastroi = list(map(int, input().split()))

ic = Counter(interes)
pc = Counter(polza)

r = 0



