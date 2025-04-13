n, b = map(int, input().split())
cl = list(map(int, input().split()))

people = 0
time = 0

for el in cl:
    people += el
    time += people
    if people < b:
        people = 0
    else:
        people -= b
time += people
print(time)





# n, b = map(int, input().split())
# cl = list(map(int, input().split()))
#
# stack = []
# time = 0
# for i in range(n):
#     stack.append([cl[i], i])
#     bn = b
#     while bn > 0:
#         if len(stack) == 0:
#             break
#         if stack[0][0] > bn:
#             stack[0][0] -= bn
#             time += bn*(i - stack[0][1] + 1)
#             bn = 0
#         elif stack[0][0] == bn:
#             time += bn * (i - stack[0][1] + 1)
#             stack.pop(0)
#             bn = 0
#         else:
#             bn = b - stack[0][0]
#             time += stack[0][0] * (i - stack[0][1] + 1)
#             stack.pop(0)
# for el in stack:
#     time += el[0] * (n - el[1] + 1)
# print(time)