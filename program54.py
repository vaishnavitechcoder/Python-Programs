class rectangle():
    def __init__(self,l,w):
        self.length = 1
        self.width = w

    def area(self):
        return self.length*self.width

newrectangle = rectangle(12,10)
print(newrectangle.area())
