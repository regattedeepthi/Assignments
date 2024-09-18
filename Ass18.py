#Dmart Task 
items = {
    "oil": {"price": 150, "quantity": 2},      
    "brush": {"price": 40, "quantity": 5},     
    "vim": {"price": 50, "quantity": 3},       
    "boost": {"price": 200, "quantity": 1}      
}
def add_item():
    while True:
         item=input("Enter the item name to add (or 'done' to finish): ") 
         if item == 'done':
              break
         quantity = int(input(f"Enter the quantity of {item}: "))
         if item in items:
            items[item]['quantity']+=quantity #update the quantity of items already in cart
         else:
          price=float(input("Enter the price of new item added "))
          items[item] = {"price": price, "quantity": quantity} 


def total(items):
   total_amount=0
   for item,total in items.items(): # item will refer the key (the name of the item), and details will refer the  value (a dictionary with the item's price and quantity).
       total_amount+= total["price"]  *total["quantity"]
   return total_amount
   

add_item()

total_bill=total(items)

print("Total bill of items ",total_bill)


 #python program of guessing number randomly    
import random
for i in range(1):
     random_number = random.randint(1,50)
     user_number  = int(input("Enter a number: "))
     if random_number==user_number:
         print("congrats you have won the game")
     elif random_number!=user_number:
         print("oops you lose the game ",random_number)
           
