n = c = s = 0

while n != 999:
    n = int(input('Enter a number, and 999 to stop: ').strip())
    if n == 999:
        break
    c += 1
    s += n
print(f'The sum is: {s}, and {c} number(s) was/were typed.')
