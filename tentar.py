a = float(input('Digite a note do aluno: '))
asub = float(a - int(a))

while a != 10:
    if 0.0<asub<0.2:
        print(int(a))
        break
    elif 0.3<asub<0.7:
        print(float(int(a)+0.5))
        break
    else:
        print(int(a+1))
        break
        
else:
    print(a)


