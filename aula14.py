a = 'aaaaa'
b = 'Bbbbbb'
c = 1.2
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)

print(formato)

string = 'b={nome2}' 'a={nome1}' 'a={nome1}' 'c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)