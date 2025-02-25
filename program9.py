lines=[]
while True:
    l=input("Enter lines:")
    if l:
        lines.append(l.upper())
    else:
        break

for l in lines:
    print(l)