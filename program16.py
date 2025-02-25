input1 = [i for i in input('Enter number:').split(',')]
result = [i for i in input1 if int(i)%2!=0]
print(','.join(map(str,result)))