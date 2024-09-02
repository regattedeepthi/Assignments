#How do you create a empty tuple on python ?
my_tuple=()
print(my_tuple)

#Write a python program to unpack atuple into several variables ?
tuplex=("Python","22.08","3")
String,float,integer=tuplex
print(String)

print(float)
print(integer)


#Write a python proram to convert tuple into a string ?
t=("I","am","learning","python")
string=' '.join(t)
print(string)

my_tuple=("python","java","javascript")
l=list(my_tuple)#converting tuple to list
print(l)
l.append("html")#add elemnt to list
print(l)
my_tuple=tuple(l)#and again convert list to tuple
print(my_tuple)
 
#Write a python program to find most frequent element in tuple ?
ntuple=(1,2,3,4,5,2,3)
nlist=[]
for i in ntuple:
    if ntuple.count(i)>1:
        if i not in nlist:
            nlist.append(i)
print(nlist)           


