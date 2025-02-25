input1 = [i for i in input('Enter numbers:').split(',')]
a = []
for j in input1:
    i = int(j,2)
    if i%5==0:
        a.append(j)
    else:
        pass

print(' '.join(a))
    