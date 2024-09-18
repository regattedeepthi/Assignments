#1.Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple.
#Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)
def convert(data):
    result=[]
    for item in data:
        if isinstance(item,tuple):
            result.extend(convert(item))
        else:
            result.append(item)
    return tuple(result)
data =((1,2),(3,4))
print(convert(data))

#another way

nested_tuple = (1, (2, 3), (4, 5, 6))
flattened_tuple = []
for num in nested_tuple:
    if isinstance(num,tuple):
        flattened_tuple.extend(num)
    else:
        flattened_tuple.append(num)
print (tuple(flattened_tuple))   

nested_tuple = (1, (2, 3), (4, 5, 6))
flattened_tuple = []
for i in nested_tuple:
     if isinstance(i, tuple):
    
       for j in i:
        flattened_tuple.append(j)
     else:
        flattened_tuple.append(i)    
print(tuple(flattened_tuple))





#2.Write a Python program to sort a tuple of tuples based on the second element
#of each tuple.
#Example Tuple: ((1, 2), (3, 1), (5, 0))Expected Output: ((5, 0), (3, 1), (1, 2))"""
students=(('vishnu',20),('Arvind',7),('John',15),('Ravi',32))
students_list=sorted(list(students),key=lambda x:x[1])
print(tuple(students_list))

nested_tuple = (1, (2, 3), (4, 5, 6))
flattened_tuple = []
for i in nested_tuple:
     if isinstance(i, tuple):
    
       for j in i:
        flattened_tuple.append(j)
     else:
        flattened_tuple.append(i)    
print(tuple(flattened_tuple))