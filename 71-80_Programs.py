"""#Program 71
#Program to reverse a string.
word=input("Enter a string: ")
reverse=""
for i in range(len(word)-1,-1,-1):
    reverse+=word[i]

print("Reversed string is: ",reverse)

#Program 72
#Program to check whether a string is a palindrome
word=input("Enter string: ")
reverse=""
original=word
for i in range(len(word)-1,-1,-1):
    reverse+=word[i]
    
if original==reverse:
    print("String is a palindrome.")
else:
    print("String is not a palindrome.")
    
#Program 73
#Program to convert a string to uppercase and lowercase without inbuilt case functions.
text=input("Enter string: ")
uppercase=""
lowercase=""
for i in range(len(text)):
    asci=ord(text[i])
    if 65<= asci <=90:
        asci=asci+32
        character_1=chr(asci)
        lowercase+=character_1
        uppercase+=text[i]
    elif 97 <=asci <=122:
        asci=asci-32
        character_2=chr(asci)
        uppercase+=character_2
        lowercase+=text[i]
    else:
        lowercase+=text[i]
        uppercase+=text[i]
    
print("String after conversion into lowercase: ",lowercase)
print("String after conversion into uppercase: ",uppercase)

#Program 74
#Program to count the frequency of each character in a string.
text=input("Enter Text: ")
visited=""
count=0
for i in range(len(text)):
    if text[i] not in visited:
        count=0
        for j in range(len(text)):
         if text[i]==text[j]:
            count+=1
        print(text[i],"appears",count,"times")
        visited+=text[i]
        

#Program 75
#Program to remove all spaces from a string.
string=input("Enter a string: ")
space=" "
new_string=""
for i in range(len(string)):
    if string[i]!=space:
        new_string+=string[i]
        
print("New string after removing spaces is: ",new_string)

#Program 76
#Program to check whether two strings are anagrams of each other
string1=input("Enter string1: ")
string2=input("Enter string2: ")
visited=""
is_anagram=True

if len(string1)!=len(string2):
    is_anagram=False
else:
    for i in range(len(string1)):
        if string1[i] not in visited:
        
         count1=0
         for j in range(len(string1)):
            if string1[i]==string1[j]:
                count1+=1
                
        count2=0
        for j in range(len(string2)):
            if string1[i]==string2[j]:
                count2+=1
                
        if count1 != count2:
            is_anagram=False
            break               
                
        visited+=string1[i]
            
if is_anagram:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
          
#Program 77
#Program to find the first non-repeating character in a string.
word=input("Enter string: ")
frequency=0
visited=""

for i in range(len(word)):
    if word[i] not in visited:
     frequency=0
     for j in range(len(word)):
        if word[i]==word[j]:
            frequency+=1
    
    if frequency==1:
        print("First non repeting character in a string is",word[i])
        break
        
#Program 78
#Program to replace all occurrences of a character with another character in a string.
text0=input("Enter string: ")
text1=input("Enter character to replace: ")
text2=input("Enter new character to replace with: ")
new_string=""

for i in range(len(text0)):
    if text0[i]==text1:
        new_string+=text2
    else:
        new_string+=text0[i]
        
print("New string is: ",new_string)

#Program 79
#Program to toggle the case of each character in a string.
text=input("Enter string: ")
toggle=""
for i in range(len(text)):
    asci=ord(text[i])
    if 65<= asci <=90:
        asci=asci+32
        character=chr(asci)
        toggle+=character
    elif 97<= asci <= 122:
        asci=asci-32
        character=chr(asci)
        toggle+=character
    else:
        toggle+=text[i]

print("String after toggling is: ",toggle)#Program 79
#Program to toggle the case of each character in a string.
text=input("Enter string: ")
toggle=""
for i in range(len(text)):
    asci=ord(text[i])
    if 65<= asci <=90:
        asci=asci+32
        character=chr(asci)
        toggle+=character
    elif 97<= asci <= 122:
        asci=asci-32
        character=chr(asci)
        toggle+=character
    else:
        toggle+=text[i]

print("String after toggling is: ",toggle)

#Program 80
#Program to read n elements into an array and print them.
#We are in python for now we will use list
choice=int(input("Enter no of elements: "))
elements=[]
for i in range(1,choice+1):
    enter=input("Enter number: ")
    elements.append(enter)
    
print("Elements stored in list are: ")
for i in range(len(elements)):
    print(elements[i])"""
    
    




        
        
        
    
    
    