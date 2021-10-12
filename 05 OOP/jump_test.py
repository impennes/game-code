end = int(input('Adj meg egy határértéket! '))
start = 10

up = True
index = start
while index < end:
    if index == 0:
        up = False
    if up:
        index -= 1
    else:
        index += 1
    print(f'{index=}  {index**2=}')
