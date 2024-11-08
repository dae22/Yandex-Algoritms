sp = input()

stek = []
os = {'(':1, '{':2, '[':3}
zs = {')':1, '}':2, ']':3}
flag = 'yes'
for el in sp:
    if el in os:
        stek.append(el)
    else:
        if len(stek) != 0 and zs[el] == os[stek[-1]]:
            stek.pop(-1)
        else:
            flag = 'no'
            break

if len(stek) == 0:
    print(flag)
else:
    print('no')