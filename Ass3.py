#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
l=[x for x in range(2000,3201) if x%7==0 and x%5!=0]
print(l)

#2.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 
n=int(input("enter the number"))
l1={i:i*i for i in range(1,n+1)}
print(l1)

#3.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98') 
numbers=input("enter the numbers: ").split(",")
list=list(numbers)
print(list)
tuple=tuple(list)
print(tuple)

#4.Write a program that accepts a comma separated sequence of words as input and prints the words ina comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without, hello, bag, world Then, the output should be: bag,hello,without,world
words=input("enter a words: ").split(",")
a=[i for i in words]
a.sort()
print(','.join(a))

# 5.Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3 
sentence=input("enter the sentence: ")
letter_count=0
digit_count=0
for i in sentence:
    if i.isalpha():
        letter_count=letter_count+1
    elif i.isdigit():
        digit_count=digit_count+1
print("number of letters: ",letter_count)
print("number of digits: ",digit_count)

#6.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9 
s=input("enter the sentence:  ")
uppercase=0
lowercase=0
for char in s:
    if char.isupper():
        uppercase+=1
    elif char.islower():
        lowercase+=1
print("number of uppercase letter are: ",uppercase)
print("number of lowercase letters are: ",lowercase)



#7.Write a program that computes the net amount of a bank account based a transaction log from console input.The transaction log format is shown as following: D 100 W 200 D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500


net_amount = 0

while True:
    transaction = input("Enter transaction (as 'D amount' or 'W amount') or 'done' to finish: ")

    if transaction.lower() == "done":
        break

    
    transaction_type, amount = transaction.split()
    amount = int(amount)

    
    if transaction_type == "D":
        net_amount += amount
    elif transaction_type == "W":
        net_amount -= amount


print("Net Amount:", net_amount)