steck = []
for el in input().split():
    if el.isdigit():
        steck.append(int(el))
    else:
        steck[-2] = eval(f'{steck[-2]}{el}{steck[-1]}')
        steck.pop(-1)
print(steck[0])
