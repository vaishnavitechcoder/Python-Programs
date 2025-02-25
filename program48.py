a = [1,2,3,4,5,6,7,8,9,10]
res1 = list(filter(lambda num: num%2 ==0, a))
res2 = list(map(lambda num: num**2, a))
print(res1)
print(res2)