ex = list(input().strip())

flag = True
for i in range(len(ex)):
    while ex[i] == ' ': # and ex[i] == ex[i+1]:
        if ex[i-1].isdigit() and ex[i+1].isdigit():
            flag = False
            break
        ex.pop(i)
    if i == len(ex)-2 or not flag:
        break
if ex[-1] in ('-', '+', '*'):
    flag = False

stack = []
postfix = []
znak = {'-': 1, '+': 1, '*': 2}
open = 0
operand = ''
for i in range(len(ex)):
    if ex[i].isalpha():
        flag = False
        break
    elif ex[i].isdigit():
        operand += ex[i]
        if i == len(ex)-1 or not ex[i+1].isdigit():
            postfix.append(operand)
            operand = ''
    else:
        if ex[i] in ('-', '+', '*'):
            if not ex[i-1].isdigit() and ex[i-1] != ')':
                flag = False
                break
            if not stack:
                stack.append(ex[i])
            else:
                while stack and stack[-1] != '(' and znak[stack[-1]] >= znak[ex[i]]:
                    postfix.append(stack.pop(-1))
                stack.append(ex[i])
        elif ex[i] == '(':
            if ex[i-1].isdigit():
                flag = False
                break
            stack.append(ex[i])
            open += 1
        elif ex[i] == ')':
            if ex[i-1] in ('-', '+', "*") or open <= 0:
                flag = False
                break
            while stack and stack[-1] != '(':
                postfix.append(stack.pop(-1))
            stack.pop(-1)
            open -= 1
            if open < 0:
                flag = False
                break
        else:
            flag = False
            break
if open > 0:
    flag = False
for el in reversed(stack):
    postfix.append(el)

if flag:
    steck = []
    for el in postfix:
        if el.isdigit():
            steck.append(int(el))
        else:
            steck[-2] = eval(f'{steck[-2]}{el}{steck[-1]}')
            steck.pop(-1)
    print(steck[0])
else:
    print('WRONG')