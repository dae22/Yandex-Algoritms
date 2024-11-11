n = int(input())
prior = list(input())
start = list(input())

inf = {'[': ']', ']': '[', '(': ')', ')': '('}
op, cl = ['[', '('], [']', ')']
stack, fnl = [], start.copy()
s, f = 0, len(fnl)

go = prior.index('[')
ko = prior.index('(')

for el in start:
    if s == 0:
        stack.append(el)
        s += 1
    elif el in op:
        stack.append(el)
        s += 1
    elif el in cl:
        stack.pop()
        s -= 1


while s + f < n:
    if s > 0:
        el = prior[min(prior.index(inf[stack[-1]]), go, ko)]
        if el in cl:
            f += 1
            s -= 1
            stack.pop()
            fnl.append(el)
        else:
            stack.append(el)
            fnl.append(el)
            s, f = s+1, f+1
    else:
        el = prior[min(go, ko)]
        stack.append(el)
        fnl.append(el)
        s, f = s+1, f+1

for el in reversed(stack):
    fnl.append(inf[el])

print(''.join(fnl))
