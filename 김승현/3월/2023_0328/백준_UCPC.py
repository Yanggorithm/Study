string = input()

UCPC = 'UCPC'
result = ''
idx = 0
for i in string:
    if i.isupper() == 1 and i == UCPC[idx]:
        result += i
        idx += 1

    if len(result) == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')

