#list operators
l1=[1,2,3,4,7,5]
l2=[3,6,7,0,8,9]
print(l1+l2)
print(l1*2)

#comparing of two lists
x=["apple","banana","cat"]
y=["Apple","Banana","Cat"]
print(x>y)#true because as per ASCII values

a=[1,2,3,4,5]
b=[1,2,3,4,5,6,7,8,9]
print(a>b)#false because a has less elements compared to b

a=[100,2,4,6]
b=[1,2,4,6]
print(a>b)#True because fisrt elemnt is greater 


#memebership checking
a=[1,5,8,10]
b=[21,5,7,0]
print(len(a))
print(5 in b)
print(21  not in a )

#nested list
n=[1,2,3,4,[2,3,4]]
print(len(n))
print(n[4][2])
 
x=[[1,2,3],[3,4,5],[5,6,7]]
for i in x:
    print(i)

#accesing
x=[[1,2,3],[4,5,6],[7,8,9]]
for i in x:
    for k in i:
      print(k, end=" ")
    print(" ")       
    

#list comprehensions
l=[i for i in range(1,10)]
print(l)

l=[x for x in range(1,30) if x%2==0]
print(l)#output is numbers b/w even numbers b/w 1-30

l=[x*x for x in range(10)]
print(l)#output is squre of number upto 10

l=[i+10 for i in range(15)]
print(l)






