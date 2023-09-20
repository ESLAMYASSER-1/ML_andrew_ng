n = input('enter a number:')
while True:
    m = input('enter a number:')
    if m == "#":
        break
    if n == m:
        print(n + ' is repeated')
        break
    n = m