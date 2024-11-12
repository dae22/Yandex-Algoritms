ex = list(input().strip())

for i in range(len(ex)):
    while ex[i] == ' ' and ex[i] == ex[i+1]:
        ex.pop(i+1)
    if i == len(ex)-2:
        break
print(ex)
stack = []
postfix = []
znak = {'-': 1, '+': 1, '*': 2}
open = 0
operand = ''
flag = True
for i in range(len(ex)):
    if ex[i].isalpha():
        flag = False
        break
    elif ex[i] == ' ':
        if ex[i-1].isdigit() and ex[i+1].isdigit():
            flag = False
            break
    elif ex[i].isdigit():
        operand += ex[i]
        if i == len(ex)-1 or not ex[i+1].isdigit():
            postfix.append(int(operand))
            operand = ''
    else:
        if ex[i] in ('-', '+', '*'):
            if not ex[i-1].isdigit():
                flag = False
                break
            if not stack:
                stack.append(ex[i])
            else:
                while stack[-1] != '(' and znak[stack[-1]] >= znak[ex[i]]:
                    postfix.append(stack.pop(-1))
                stack.append(ex[i])
        elif ex[i] == '(':
            if ex[i-1].isdigit():
                flag = False
                break
            stack.append(ex[i])
            open += 1
        elif ex[i] == ')':
            if ex[i-1] in ('-', '+', "*"):
                flag = False
                break
            while stack and stack[-1] != '(':
                postfix.append(stack.pop(-1))
            stack.pop(-1)
            open -= 1
        else:
            flag = False
            break


print(postfix)
print(stack)

for el in reversed(stack):
    postfix.append(el)

print(postfix)
print(flag)






# try:
#     print(eval(input()))
# except:
#     print('WRONG')