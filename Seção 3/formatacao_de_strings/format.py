a = 'AAA'
b = 'BBBB'
c = 1.1

string1 = 'A = {} B = {} C = {}'
formato1 = string1.format(a, b, c)

print(formato1)

formato2 = 'A = {0} A = {0} C = {2}'.format(a,b,c)

print(formato2)

formato3 = 'C = {:.2f}'.format(c)

print(formato3)

formato4 = 'A = {nome1} B = {nome2} C = {nome3}'.format(
    nome1=a,
    nome2=b,
    nome3=c
)

print(formato4)