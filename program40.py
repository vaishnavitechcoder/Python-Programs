def print_list():
    n=[]
    b=input("enter power:")
    for i in range(1,21):
        n.append(i**int(b))
    print(n[-5:])
print_list()