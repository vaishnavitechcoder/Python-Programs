a = input("Enter str1:")
b = input("Enter str2:")
def len_str(a,b):
    if len(a)>len(b):
        print("a is max length")
    elif len(a)==len(b):
        print("a and b is same length")
    else:
        print("b is max_length")
    return
print(len_str(a,b))