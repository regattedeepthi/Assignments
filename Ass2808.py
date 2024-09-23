account=int(input("enter the number"))
pin=int(input("enter the number"))

balance=10000
if account==1246100 and pin==789:
    choice =int(input("Enter the choice \n 1 to current balance\n enter 2 withdrawl\n enter 3 to balnace enquiry"))
    if choice==1:
      print("your current balance is  "+ str(balance))
    
    elif choice==2:
        amount=int(input("enter the amount"))
        if(amount>balance):
            print("Insufficient funds")
        else:
            balance-=amount
            print("Withdrawl is successfull")
    elif choice==3:
     
     print("current balance is "+str(balance))
    else:
       print("choose the correct option")
else:
    print("Invalid account number or PIN")




