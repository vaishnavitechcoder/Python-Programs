def print_dict():
    a = {i:i**2 for i in range(1,21)}
    print(a.items())
    print(a.values())

print(print_dict())