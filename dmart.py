items = {
    'oil': 3.0,
    'brush': 1.5,
    'vim': 2.0,
    'boost': 1.0
}




def calculate_bill(purchased_items):
    total = 0
    for item, quantity in purchased_items.items():
        total += items[item] * quantity
    return total
 
# Taking multiple items input from the user
purchased_items = {}
while True:
    item = input("Enter the item (or type 'done' to finish): ").lower()
    if item == 'done':
        break
    if item in items:
        quantity = int(input(f"Enter the quantity of {item}: "))
        if item in purchased_items:
            purchased_items[item] += quantity
        else:
            purchased_items[item] = quantity
    else:
        print("Item not found. Please enter a valid item.")
 
# Calculate the total bill
total_bill = calculate_bill(purchased_items)
print(f"The total bill is: ${total_bill:.2f}")
 