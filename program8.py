input1 = [i for i in input("Enter string:").split(',')]
str1 = sorted(input1)
print(','.join(map(str,str1)))