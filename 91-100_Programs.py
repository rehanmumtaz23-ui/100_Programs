"""#Program 91
#Program to find the sum of all even-indexed and odd-indexed elements separately
numbers=[10,20,30,40,50,60,70,80,90,100]
even_sum=0
odd_sum=0

for i in range(len(numbers)):
    if i%2==0:
        even_sum+=numbers[i]
    else:
        odd_sum+=numbers[i]
        
print("Even indexes sum is: ",even_sum)
print("Odd indexes sum is: ",odd_sum)

#Program 92
#Program to check whether a number is prime, using a function/method.
number=int(input("Enter a number: "))
def is_prime(number):
    for i in range(2,number):
        if number%i==0:
            print("Number is not prime")
            break
    else:
        print("Number is prime.")
        
is_prime(number)

#Program 93
#Program to print all prime numbers between two given numbers a and b
number1,number2=map(int,input("Enter two numbers: ").split())

def is_prime(number1,number2):
    for i in range(number1,number2):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)

print("Prime numbers are:")
is_prime(number1,number2)

#Program 94
#Program to find the sum of digits of a number repeatedly until a single digit remains

number=int(input("Enter a number: "))
while number>9:
    sum=0
    while number>0:
        digit=number%10
        sum+=digit
        number=number//10
    
    number=sum

print("Sum is:",number)

#Program 95
#Program to count the number of prime digits present in a number n
number=int(input("Enter a number: "))
count=0

while number>0:
    digit=number%10
    number=number//10
    for i in range(2,digit):
        if digit%i==0:
            break
    else:
        count+=1               
            
print("Number of prime digits in a number are: ",count)

#Program 96
#Program to check whether a number is a palindrome and a prime at the same time
number=int(input("Enter a number: "))
reversed=0
original=number

while number>0:
    digit=number%10
    number=number//10
    reversed=reversed*10+digit
    

is_palindrome=original==reversed
is_prime=True

if original < 2:
    is_prime=False
else:
    for i in range(2,original):
        if original%i==0:
            is_prime=False
            break
if is_palindrome and is_prime:
    print("Number is palindrome and prime")
else:
    print("Number is not palindrome and prime")
    
    
#Program 97
#Program to find the largest and smallest number that can be formed using the digits of n.
number=int(input("Enter a number: "))
lis=[]
smallest=0
largest=0
while number>0:
    digit=number%10
    number=number//10
    lis.append(digit)
    lis.sort()
    
for i in range(len(lis)):
    smallest=smallest*10+lis[i]
    
lis.sort(reverse=True)

for i in range(len(lis)):
    largest=largest*10+lis[i]

print("Largest number which can be formed is: ",largest)
print("Smallest number which can be formed is: ",smallest)

#Program 98
#Program to convert a decimal number into its binary equivalent.
number=int(input("Enter a number: "))
binary=0
reversed=0
while number>0:
    reminder=number%2
    number=number//2
    binary=binary*10+reminder
    
while binary>0:
    digit=binary%10
    binary=binary//10
    reversed=reversed*10+digit

print(reversed)

#Program 99
#Program to convert a binary number into its decimal equivalent.
number=int(input("Enter a number: "))
power=1
result=0
while number>0:
    digit=number%10
    number=number//10
    binary=digit*power
    result+=binary
    power=power*2
    
    
print(result)

#Program 100
#Program to display a menu that lets the user repeatedly choose any of the above tasks until they choose to exit.

while True:
    print("____PYTHON MENUE____")
    print("1)Binary to decimal conversion.")
    print("2)Decimal to binary conversion.")
    print("3)Exit")
    
    choice=int(input("Enter a choice:"))
    
    if choice==1:
        number=int(input("Enter a number: "))
        binary=0
        reversed=0
        while number>0:
         reminder=number%2
         number=number//2
         binary=binary*10+reminder
    
        while binary>0:
         digit=binary%10
         binary=binary//10
         reversed=reversed*10+digit
    
        print(reversed)

    elif choice==2:
        number=int(input("Enter a number: "))
        power=1
        result=0
        while number>0:
         digit=number%10
         number=number//10
         binary=digit*power
         result+=binary
         power=power*2
    
        print(result)
        
    elif choice==3:
        break
    
    else:
        print("Invalid choice.")"""
        
    
        



