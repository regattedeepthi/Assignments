#index and length of the striong
name="Vishrudh"
length=len(name)
for i in range(length):
    if name[i]=="h":
        print(i)
        


#concatenating
str1="I"
str2="am"
str3="learning"
str4="python"
str=(str1+" "+str2+" "+str3+" "+str4)
print(str)

#repitition-----> repeats the string
pattern="*"
result=pattern*6
print(result)

#find()
text="Mobile Application are designing"
Index=text.find("A")
Index1=text.find("Application")
Index2=text.find("are",7)
Index3=text.find("a",0,20)
Index4=text.find("web")

print( Index)
print(Index1)
print(Index2) 
print(Index3)
print(Index4)

#rfind
s="learning python is very easy"
index=s.rfind("e")
print(index)
index=s.rfind("y")
print(index)
index=s.rfind("a")
print(index)


#lfind
s="learning python is very easy"
index=s.find("a")
print(index)

#count()---> frequency of string
word="aaabbbccdddd"
print(word.count("d"))

#strip()---> removes the spaces
word=" Python "
print(len(word))
sw=word.strip()
print(len(sw))













