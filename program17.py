Balance=0
while True:
    n = input("Enter the operation:\n")
    operation=n.split()   
    value=operation[0]
    amount=int(operation[1])
    if value=="D":
        Balance+=amount
    elif value=="W":
        if amount>Balance:
            print("Insufficient balance")
        else:
            Balance-=amount
    else:
        pass
    ch = input("Are you sure you want to exit if then enter y other wise n: ")
    if ch== "y" or ch == "Y":
        break
    
    
    print("Total Balance", Balance )
print ("Final Balance", Balance)