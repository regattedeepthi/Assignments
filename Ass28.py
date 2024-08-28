#Membership checking
n1=['ram','pavan','vishnu','harsha']
if "pavan" in n1:
    print("pavan is in the list")


#replace()-----> string replaced with new string
name="Harshith"
print(name.replace("r","n"))



#using for loop replacing numbers in list
n=[2,3,0,8,9]
fn=0
sn=1
for i in range(len(n)):
    if n[i]==fn:
      n[i]=sn
print(n)

#sum of numbers in list using for loop
number= [10, 20, 30, 40]
total=0
for n in number:
    total += n
    print(total)

#counting number of vowels in a string
string ="hello world"
vowels="aeiou"
count=0
for i in string:
    if i in vowels:
        count=count+1
        print(count)


#join()
l=["ram","krishna","gopi","shiva"]
print(len(l))
s="+".join(l)
print(s)
print(len(s))


#startswith
s= "konidala pavan"
print(s.startswith("konidala"))
#endswith
s="skywaves software"
print(s.endswith("software"))
print(s.endswith("company"))

#uppercase
s="skywaves"
print(s.upper())
#lowercase
s="LearNING"
print(s.lower())

#swapcase
s="python"
print(s.swapcase())
s="LEARNING IS EASY"
print(s.swapcase())

#title
s="learning python is easy"
print(s.title())

#capitalize
s="automation"
print(s.capitalize())

