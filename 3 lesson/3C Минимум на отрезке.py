n, k = map(int, input().split())
nums = list(map(int, input().split()))

dq = []
if k == n:
    print(min(nums))
elif k == 1:
    for el in nums:
        print(el)
else:
    for el in enumerate(nums):
        if not len(dq):
            dq.append(el)
        else:
            if dq[0][0] < el[0] - k + 1:
                dq.pop(0)
            if not len(dq) or dq[-1][1] <= el[1]:
                dq.append(el)
            else:
                while len(dq) and dq[-1][1] > el[1]:
                    dq.pop(-1)
                dq.append(el)
        if el[0] > k-2:
            print(dq[0][1])
