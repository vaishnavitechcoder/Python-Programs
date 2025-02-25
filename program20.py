class divisible():
    def __init__(self,n):
        self.n=n
    def generator(self):
        for number in range(0,self.n+1):
            if number%7==0:
                yield number

n = 50
divisible_by_seven = divisible(n)
for num in divisible_by_seven.generator():
    print(num)