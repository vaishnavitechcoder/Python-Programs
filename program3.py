def is_factorial(n):
    if n==0:
        return 1
    else:
        return n*is_factorial(n-1)

print(is_factorial(8))