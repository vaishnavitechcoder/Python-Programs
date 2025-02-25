c = 50
h = 30
f = []
d = [int(i) for i in input("Enter Numbers:").split(',')]
l = len(d)
for i in range(l):
    q = (2*c*d[i])/h**(0.5)
    f.append(round(q))

for i in range(l):
  if i==l-1:
    print(f[i],end="")
  else:
    print(f[i],end=',')


