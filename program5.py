class program():
    def __init__(self):
        self.name=''
    def getString(self):
        self.name=input()
    def printString(self):
        print(self.name.upper())

name=program()
name.getString()
name.printString()
        