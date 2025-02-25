input1 = [i for i in input('Enter sentence:').split(' ')]
upper = 0
lower = 0
for i in input1:
    for j in i:
        if j.isupper():
            upper+=1
        elif j.islower():
            lower+=1
print('UPPERCASE',upper)
print('LOWERCASE',lower)