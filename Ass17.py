
#Create a dictionary where the keys are tuples representing coordinates (x, y) and the values are city names. Write a Python program to print the city name for a given coordinate. Example Dictionary: #{(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"} 
# # Input: (40.7128, -74.0060) # Expected Output: "New York"

city_dict = {(40.7128, -74.0060): "New York",(34.0522, -118.2437): "Los Angeles",(41.8781, -87.6298): "Chicago"}
def get_city_name(coordinates):
    return city_dict.get(coordinates, "City not found")


input_coordinates = (40.7128, -74.0060)
city_name = get_city_name(input_coordinates)
print(city_name) 


#Write a Python program to sort a tuple of tuples based on the second element of each tuple. python 
# # Example Tuple: ((1, 2), (3, 1), (5, 0)) # Expected Output: ((5, 0), (3, 1), (1, 2))
emp_salary=((101,20000),(102,50000),(103,48000),(104,10000),(105,35000))
emp_salary_list=sorted(list(emp_salary),key=lambda x:x[1])
print(tuple(emp_salary_list))

#Write a Python program to find the minimum and maximum elements in a tuple of integers. python # Example Tuple: (10, 20, 5, 40, 25)
 # Expected Output: Min: 5, Max: 40
tup=()
n=int(input("enter the number of elements to enter "))
for x in range(n):
 tup+=(int(input("enter the element ")),)
print(tup) 
min_value=min(tup,key=lambda x:x)
max_value=max(tup,key=lambda x:x)
print("minimum value of tuple ",min_value)
print("maximum value of tuple ",max_value)

#Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple. python
#  # Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)
nested_tuple = (1, (2, 3), (4, 5, 6))
flattened_tuple=[]
for i in nested_tuple:
 if isinstance(i,tuple):
  flattened_tuple.extend(i)
 else:
  flattened_tuple.append(i)
print(tuple(flattened_tuple)) 
