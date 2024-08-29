#How to create a list
l1=list("python")
print(l1)

#creating a list using split()
name="p y t h on"
s1=name.split()
print(s1)

#accessing the elements from list
list=[1,2,3,4,7,8]
print(list[0])
#to get odd numbers
print(list[0:6:2])
#to get even numbers
print(list[1:7:2])


list=["SELENIUM","CUCUMBER","JAVA","PYTHON"]
#adding a element through append()----> add elements at end of the list
list.append("AUTOMATION")
print(list)

#adding element through insert method--->add elements in specified index position
list.insert(2,"1992")
print(list)

l1=["python","is","high level"]
l2=["and","interpreted language"]
#adding two lists with extend method
#l1.extend(l2)
#print(l1)
#adding two lists with '+'operator
l=l1+l2
print(l)

#iterating through list
list=[10,20,30,40,50]
for i in list:
    print(i)

matrix=[2,4,6,8,10,12,15]
#removing elements using pop()-----> removes and returns last element
matrix.pop()
print(matrix)
#removing the elements using remove()--->removes specified element from list
matrix.remove(10)
print(matrix)


#reverse the elements using reverse()
names=["ram","krishna","shiva"]
names.reverse()
print(names)
print(names[::-1])

#sort()---> returns ascending order of list
l=[1,2,6,4,16,14,18]
l.sort()
print(l)