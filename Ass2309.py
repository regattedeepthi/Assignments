#Write a program to get phone number as output if we give name as input in dictionary
Phone_book={}
while True:
   
    name = input("Enter a name (or type 'exit' to finish): ")
    if name.lower() == 'exit':
       break
    number = int(input("Enter a value: "))
    Phone_book[name] = number
    print(Phone_book)
   
def get_number_by_name(dictionary):
    search_number = input("Enter a name to get number (or type 'exit' to finish): ")
    if search_number.lower() == 'exit':
        return False  
    result = dictionary.get(search_number, "name  not found.")
    print(search_number,":", result)
    return True  
while True:
    if not get_number_by_name(Phone_book):
        break
print("Your dictionary:", Phone_book)

 #other way
dic = {}
n = int(input("Enter the number of entity: "))
 
for i in range(n):
     name = input("Enter the name: ")
     number = input("Enter the number: ")
     dic[name] = number
 
def find():
     nam = input("Enter the name to get number: ")
     if nam in dic:
        print(dic[nam])
find()
 
 

 