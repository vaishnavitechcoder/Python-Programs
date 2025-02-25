input1 = [i for i in input('Enter sentence:').split(' ')]
letter = 0
digits = 0
for j in input1:
    for i in j:
        if j.isdigit():
            digits+=1
        else:
            letter+=1
    
print('LETTERS',letter)
print('DIGITS',digits)

