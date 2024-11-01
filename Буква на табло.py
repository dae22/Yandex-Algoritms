def whos_that_pokemon(tab):
    if len(taba) == 0:
        return 'X'
    elif i_check(tab):
        return 'I'
    elif o_check(tab):
        return 'O'
    elif c_check(tab):
        return 'C'
    elif l_check(tab):
        return 'L'
    elif h_check(tab):
        return 'H'
    elif p_check(tab):
        return 'P'
    else:
        return 'X'


def i_check(tab):
    l, r = tab[0].find('#'), tab[0].rfind('#')
    for row in tab:
        if row[l:r+1] == '#' * (r-l+1):
            if '.' in row[l:r+1] or '#' in row[0:l] or '#' in row[r+1:]:
                return False
        else:
            return False
    return True


def o_check(tab):
    l, r = tab[0].find('#'), tab[0].rfind('#')
    flu, fld, ll = 0, 0, 0
    for i in range(len(tab)):
        if '#' in tab[i][0:l] or '#' in tab[i][r+1:]:
            return False
    for i in range(len(tab)):
        if '.' in tab[i][l:r+1]:
            break
        else:
            flu += 1
    for i in range(-1, -len(tab)-1+flu, -1):
        if '.' in tab[i][l:r+1]:
            break
        else:
            fld += 1
    if fld == 0 or flu == 0:
        return False
    le, re = tab[flu][l:r+1].find('.')+l, tab[flu][l:r+1].rfind('.')+l
    if le == l or re == r:
        return False
    for i in range(flu, len(tab)-flu-fld+1):
        if tab[i][le:re+1] != '.'*(re-le+1) or '.' in tab[i][l:le] or '.' in tab[i][re+1:r+1]:
            return False
        ll += 1
    if ll == 0:
        return False
    else:
        return True


def c_check(tab):
    l, r = tab[0].find('#'), tab[0].rfind('#')
    flu, fld, ll = 0, 0, 0
    for i in range(len(tab)):
        if '#' in tab[i][0:l] or '#' in tab[i][r+1:]:
            return False
    for i in range(len(tab)):
        if '.' in tab[i][l:r+1]:
            break
        else:
            flu += 1
    for i in range(-1, -len(tab)-1+flu, -1):
        if '.' in tab[i][l:r+1]:
            break
        else:
            fld += 1
    if fld == 0 or flu == 0:
        return False
    le, re = tab[flu][l:r+1].find('.')+l, tab[flu][l:r+1].rfind('.')+l
    if re != r or le == l:
        return False
    for i in range(flu, len(tab)-flu-fld+1):
        if tab[i][le:re+1] != '.'*(re-le+1):
            return False
        ll += 1
    if ll == 0:
        return False
    else:
        return True


def l_check(tab):
    tabl = tab[::-1]
    l, r = tabl[0].find('#'), tabl[0].rfind('#')
    for i in range(len(tab)):
        if '#' in tab[i][0:l] or '#' in tab[i][r+1:]:
            return False
    flag = True
    fl, ll = 0, 0
    for row in tabl:
        if flag:
            if '.' not in row[l:r+1]:
                fl += 1
            else:
                flag = False
                le = row[l:r+1].find('.')+l
                ll += 1
                if '#' in row[le:r+1]:
                    return False
        elif not flag and '#' in row[le:r+1]:
            return False
    if fl < 1 or ll < 1:
        return False
    return True


def h_check(tab):
    l, r = tab[0].find('#'), tab[0].rfind('#')
    le, re = tab[0][l:r+1].find('.')+l, tab[0][l:r+1].rfind('.')+l
    flu, fld, ll = 0, 0, 0
    for i in range(len(tab)):
        if '#' in tab[i][0:l] or '#' in tab[i][r + 1:]:
            return False
    for i in range(len(tab)):
        if '.' in tab[i][l:le] or '.' in tab[i][re+1:r+1]:
            return False
        elif '#' in tab[i][le:re + 1]:
            break
        else:
            flu += 1
    for i in range(-1, -len(tab) - 1, -1):
        if '.' in tab[i][l:le] or '.' in tab[i][re+1:r+1]:
            return False
        elif '#' in tab[i][le:re + 1]:
            break
        else:
            fld += 1
    for i in range(flu, len(tab)-fld):
        if tab[i][l:r + 1] != '#' * (r - l + 1):
            return False
        ll += 1
    if fld == 0 or flu == 0 or ll == 0:
        return False
    else:
        return True


def p_check(tab):
    l, r = tab[0].find('#'), tab[0].rfind('#')
    flu, mll, fld, ll = 0, 0, 0, 0
    for i in range(len(tab)):
        if '#' in tab[i][0:l] or '#' in tab[i][r + 1:]:
            return False
    for i in range(len(tab)):
        if '.' in tab[i][l:r + 1]:
            break
        else:
            flu += 1
    if flu == 0:
        return False
    if flu == len(tab):
        return False
    le, re = tab[flu][l:r+1].find('.')+l, tab[flu][l:r+1].rfind('.')+l
    if le <= l or re >= r:
        return False
    for i in range(flu, len(tab)):
        if tab[i][l:r+1] == '#' * (r - l + 1):
            break
        elif '.' in tab[i][l:le] or '.' in tab[i][re+1:r+1] or '#' in tab[i][le:re+1]:
            return False
        mll += 1
    if mll == 0:
        return False
    for i in range(flu+mll, len(tab)):
        if '.' in tab[i][l:r+1]:
            break
        fld += 1
    if fld == 0:
        return False
    for i in range(flu+mll+fld, len(tab)):
        if '.' in tab[i][l:le] or '#' in tab[i][le:r+1]:
            return False
        ll += 1
    if ll == 0:
        return False
    return True


with open('input.txt', 'r') as f1:
    n = int(f1.readline().rstrip())
    taba = []
    flag = True
    for row in f1.readlines():
        if flag and '#' not in row:
            continue
        else:
            taba.append(row.rstrip())
            flag = False
    while len(taba) != 0:
        if '#' not in taba[-1]:
            taba.pop(-1)
        else:
            break

with open('output.txt', 'w') as f2:
    f2.write(whos_that_pokemon(taba))
