"""#Program 61
#Program to find the sum of the series 1 + 1/2 + 1/3 + ... + 1/n.
number=int(input("Enter a number: "))
sum=0
for i in range(1,number+1):
    div=1/i
    sum=sum+div
print("Sum of series is: ",sum)

#Program 62
#Program to find the value of x raised to the power y without using inbuilt power.
num1=int(input("Enter Base: "))
num2=int(input("Enter Exponent: "))
result=1
for i in range(1,num2+1):
    result=result*num1
        
print("Your result is: ",result)

#Program 63
#Program to print a right-angled triangle pattern of stars of height n.
number=int(input("Enter the number of rows: "))
for i in range(1,number):
    for j in range(1,i+1):
        print("*",end="")
        
    print()
    
#Program 64
#Program to print an inverted right-angled triangle pattern of stars of height n.
number=int(input("Enter the number of rows: "))
for i in range(1,number+1):
    for j in range(1,number-i+1):
        print("*",end="")
        
    print()
    

#Program 65
#Program to print a pyramid pattern of stars of height n.
number=int(input("Enter a number: "))
for i in range(1,number+1):
    for j in range(number-i):
        print(" ",end="")
    for k in range(1,2*i-1):
        print("*",end="")
        
    print()
    
#Program 66
#Program to print a number triangle (row i contains numbers 1 to i).    
number=int(input("Enter number of rows: "))

for i in range(1,number+1):
    for j in range(1,i+1):
        print(j,end="")
        
    print()
    
#Program 67
#Program to print pascals triangle for n rows

number = int(input("Enter number of rows: "))
for i in range(1, number+1):
    for j in range(number-i):
        print(" ", end="")
    for j in range(1, i+1):
        n = i-1
        r = j-1

        fact1 = 1
        for k in range(1, n+1):
            fact1 = fact1*k

        fact2 = 1
        for k in range(1, r+1):
            fact2 = fact2*k

        fact3 = 1
        for k in range(1, (n-r)+1):
            fact3 = fact3*k

        result = fact1 // (fact2*fact3)

        print(result, end=" ")

    print()
    
#Program 68
#Program to find the length of a string without using an inbuilt function
word=input("Enter your characters: ")
count=0
for i in word:
    count+=1
    
print("Leanght of charcter is: ",count)


#Program 69
#Program to count the number of vowels and consonants in a string.
word=input("Enter Text: ")
vowels=0
consonants=0

for i in word:
    if i in "AEIOUaeiou":
        vowels+=1
    elif i.isalpha():
        consonants+=1

print("Total vowels in text are: ",vowels)
print("Total consonents in text are: ",consonants)

#Program 70
#Program to count the number of words in a sentence.
sentence=input("Enter a sentence: ")
count=0
words=0
for i in sentence:
    if i==" ":
        count+=1

words=count+1
print("Total number of words in a sentence are: ",words)"""
