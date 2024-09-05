#Write a python program to  add a key to a dictionary ?
dictionary={}
size=int(input("enter the size: "))
for i in range(size):
    key=input("enter key:  ")
    value=input("enter value: ")
    dictionary[key]=value
print(dictionary)  


#Write a python program to check weather the given value is present in the dictionary or not ?
d={"name":"Roshini","age":25,"work":"Designer","Location":"Hyderabad"}
check=input("Enter the value to check: ")
if check in d.values():
    print("The value '{check}' is prsent in dictionary")
elif check not in d:
    print("The value '{check}' is not present in dictionary")


#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
d1=dict()
for x in range(1,16):
    d1[x]=x*x
print(d1)


#Write a python program to create a dictionary from the string ?
string=input("enter the string: ")
my_dict={}
for x in string:
    my_dict[x]=my_dict.get(x,0)+1
print(my_dict)   


#Write a python program to combine two dictionaries by adding values of common keys ?
dict1={"names":100,"vehicles":200,"deliveries":100,"locations":50}
dict2={"names":50,"vehicles":50,"packages":150}
for str in dict2.keys():
    if str in dict1.keys():
        dict1[str]+=dict2[str]

    else:
        dict1[str]=dict2[str]
print(dict1)       


#Write a python program to merge two python dictionaries ?
c1={"Vinod":90,"Priya":"88","Sindhu":90}
c2={"Sruthi":91,"Anand":85}
c3={**c1,**c2}
print(c3)
#using update()
c1.update(c2)
print(c1)


#Write  a python program to sort dictionary by keys or values ?
Students={"Mahesh":10,"Suresh":15,"Kavitha":14,"Anil":13}
Students=dict(sorted(Students.items(),key=lambda x:x[0]))#sorting with keys 
print(Students)
Students=dict(sorted(Students.items(),key=lambda x:x[1]))#sorting with value
print(Students)


#Write a Python program to create a dictionary from a string.  Note: Track the count of the letters from the string.
#Sample string : 'w3resource'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
string=input("enter the string: ")
my_dict={}
for x in string:
    my_dict[x]=my_dict.get(x,0)+1
print(my_dict)