n = int(input())

macros = {'+': 'stack.append(int(el[1]))', '-': 'print(stack.pop())', '?': 'print(sum(stack[-2:]))'}
stack = []
for _ in range(n):
    el = input()
    exec(macros[el[0]])
