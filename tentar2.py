import math

a = float(input('Digite a note do aluno: '))
asub = float(a - int(a))

if asub<0.3:
    print(math.floor(a))
elif 0.3<asub<0.7:
    print(float(int(a)+0.5))
else:
    print(math.ceil(a))
    