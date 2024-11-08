def r_and_blue(d):
    if 0 in d:
        if d[0] == 0 or d[2] == 0:
            return [d[0]+1, d[2]+1]
        else:
            return [d[1]+1, d[3]+1]
    elif d[0] == d[1]:
        return [d[0]+1, 1]
    option = []
    option.append([d[0]+1, d[2]+1])
    option.append([d[1]+1, d[3]+1])
    option.append([max(d[0], d[1])+1, 1])
    option.append([1, max(d[2], d[3])+1])
    return min(option, key=sum)


data = []
with open('input.txt', 'r', encoding='UTF-8') as f:
    for el in f.readlines():
        data.append(int(el.rstrip()))

with open('output.txt', 'w', encoding='UTF-8') as f1:
    f1.write(f'{r_and_blue(data)[0]} {r_and_blue(data)[1]}')

#commit