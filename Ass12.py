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





#2.Write a Python program to sort a tuple of tuples based on the second element
#of each tuple.
#Example Tuple: ((1, 2), (3, 1), (5, 0))Expected Output: ((5, 0), (3, 1), (1, 2))"""
students=(('vishnu',20),('Arvind',7),('John',15),('Ravi',32))
students_list=sorted(list(students),key=lambda x:x[1])
print(tuple(students_list))
