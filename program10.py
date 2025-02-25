input1 = [i for i in input("Enter word:").split(' ')]
int2 = sorted(set(input1))
print(' '.join(map(str,int2)))