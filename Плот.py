def NS(y1, y2, y):
    if y > y2:
        return 'N'
    elif y < y1:
        return 'S'
    else:
        return ''


def WE(x1, x2, x):
    if x > x2:
        return 'E'
    elif x < x1:
        return 'W'
    else:
        return ''


c = []
with open('input.txt', 'r', encoding='UTF-8') as f:
    for el in f.readlines():
        c.append(int(el.rstrip()))

with open('output.txt', 'w', encoding='UTF-8') as f1:
    f1.write(NS(c[1], c[3], c[5]) + WE(c[0], c[2], c[4]))