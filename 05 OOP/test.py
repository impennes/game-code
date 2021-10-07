def szamol_2():
    global x
    x += 7


def szamol():
    return x + 2


x = 6
print(szamol())
szamol_2()
print(f'{x}')