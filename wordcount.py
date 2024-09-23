 #input:"i am learning python and learnning java"

def count_words(input_string):
    word_count={}
    words=input_string.split()
    for word in words:
       word= word.lower()
       if word in word_count:
            word_count[word]+=1
       else:
            word_count[word]=1
    return word_count
total_words=count_words("I am learning python and learning java")
print(total_words)

"""
def count_char(input_string):
    char_count={}
    
    for char in input_string:
        char=char.lower()
        if char!=" ":
         if char in char_count:
            char_count[char]+=1
         else:
            char_count[char]=1
    return char_count
total_char=count_char("I am learning python and learning java")
print(total_char)
"""

def count_word_frequency(sentance):
    words = sentance.replace(" ","")
    frequncy={}
    for word in words:
        if word in frequncy:
            frequncy[word]+=1
        else:
            frequncy[word]=1
    return frequncy
sentance = "i am learning python and using python"
print(count_word_frequency(sentance))
count_word_frequency(sentance)
 