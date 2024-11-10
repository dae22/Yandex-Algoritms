n = int(input())

stack = []
pref = [0]
for _ in range(n):
    el = input()
    if el[0] == '+':
        stack.append(int(el[1:]))
        pref.append(pref[len(stack)-1] + stack[-1])
    elif el[0] == '-':
        print(stack.pop())
        pref.pop()
    elif el[0] == '?':
        k = int(el[1:])
        print(pref[-1]-pref[-k-1])






# macros = {'+': 'stack.append(int(el[1:]))', '-': 'print(stack.pop())', '?': 'print(sum(stack[-int(el[1:]):]))'}
# stack = []
# for _ in range(n):
#     el = input()
#     exec(macros[el[0]])
