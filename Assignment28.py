#Python Program to count occurrence of a given characters in string.
string="Hello world"
char='o'
print(string.count(char))

#using for loop
string="selenium is web automation tool "
count=0
char="e"
for i in string:
    if i in char:
        count=count+1
print(count)  


#Python Program to check if two Strings are Anagram.
s1=str(input("enter string"))
s2=str(input("enter string"))
l1=print(len(s1))# check the length of both strings
l2=print(len(s2))
if l1==l2:
    sorts1=print(sorted(s1)) #sorting the both strings in to char arrays
    sorts2=print(sorted(s2))

if sorts1==sorts2:
 print("s1 and s2 are anagrams")
else:
   print("s1 and s2 both are not anagrams")
   
#Python program to check a String is palindrome or not.
txt="madam"
txt2=txt[::-1] # : specify starting and ending char in reverse orderz
if (txt == txt2):
   print("string is a palindrome")
else:
   print("string is not a palindrome")


#Python program to replace the string space with a given character using replace method
string=" gmail.com"
replaced_string=string.replace(" ","@")
print(replaced_string)

#Python program to replace the string space with a given character
s="Hello world"
s2=" "
for i in range(0,len(s)):
   if s[i]== " ":
      s2=s2+ "_"
   else:
      s2=s2+s[i]
print(s2)

   
#Python program to convert lowercase char to uppercase of string.
text="abcde"
print(text.upper())


#Python program to convert lowercase vowel to uppercase in string.
s=input("enter a string")
vowels="aeiou"
for i in s:
   if i in vowels:
      upper_case=i.upper()
      str=s.replace(i,upper_case)
      print(str)


#Python program to separate characters in a given string.
x="I am learning python"
print(x.split())


#Python program to remove blank space from string.
word=" number "
print(word.rstrip())#removes right side space
print(word.lstrip())#removes left side space

#Python program to concatenate two strings using join() method.
list=["version","control"]
print(len(list))
s="_".join(list)
print(s)


#Python program to concatenate two strings without using join() method.
s1="Good"
s2="evening"
new_string="{} {}".format(s1,s2)
print(new_string)

new_string=f"{s1} {s2}"
print(new_string)


#Python program to remove repeated character from string.
text1="abbcccddd"
text2=''
for char in text1:
   if char not in text2:
      text2=text2+char
print(text1)
print(text2)

#Python program to check given character is vowel or consonant.
charat=input("enter the character")
vowels="aeiouAEIOU"
if charat in vowels:
   print("given character is vowel")
else:
   print("given character is constant")

#Python program to check given character is digit or not.
given_n=input("enter the character ")

if given_n.isdigit() is True:
   print("n is a digit")
else:
   print("n is a not a digit")
   
  
   #Python program to delete vowels in a given string.
   string=input("enter a string ")
   vowels=['a','e','i','o','u','A','E','I','O','U']
   for i in string:
      if char not in vowels:
         str=str+i
   print("string without vowels is ",str)   

#Python program to count the Occurrence Of Vowels & Consonants in a String.
vowel_count=0
consonant_count=0
variable=input("enter the string")
vowels="a,e,i,o,u,A,E,I,O,U"

for i in variable:
   if i in vowels:
      vowel_count+=1
   else:
      consonant_count+=1
     
print("count of vowels ",vowel_count)
print("count of consonants ",consonant_count)


#Python program to check given character is digit or not using isdigit() method.
char=input("enter the character")
result=print(char.isdigit())
if result == True:
   print("char is digit")

#Python program to calculate sum of integers in string.
s=input("enter the s")
sum=0
for i in s:
   if i.isdigit():
      sum+=int[i]
print("total sum of string ",sum)     

