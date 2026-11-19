"""#Program 51
#Program to check weather a number is automorphic number or not

number=int(input("Enter a number:"))
original=number
square=number**2
count=0
while number>0:
    digit=number%10
    number=number//10
    count+=1
    result=square%(10**count)
    if result==original:
        print("Number is automorphic.")
    else:
        print("Number is not automorphic.")
        
#Program 52
#Program to check weather a number is Harshad(niven) number
number=int(input("Enter a number:"))
original=number
total=0

while number>0:
    digit=number%10
    number=number//10
    total=total+digit

div=original%total
if div==0:
    print("The number is Harshad number.")
else:
    print("The number is not a Harshad number.")
    
#Program 53
#Program to find all factors of a number n
number=int(input("Enter a number:"))
print("All the factors of entered number are: ")
for i in range(1,number+1):
    if number%i==0:
        print(i)
        
#Program 54
#Program to find the numbers of the factor of a number n
number=int(input("Enter a number n: "))
count=0
for i in range(1,number+1):
    if number%i==0:
        count+=1
print("Total factors of entered number are:",count)

#Program 55
#Program to find GCD(HCF) of two numbers

number1,number2=map(int,input("Enter 2 numbers: ").split())
new_number=0
for i in range(1,min(number1,number2)+1):
    if number1%i==0 and number2%i==0:
        new_number=i

print("The HCF of 2 numbers is",new_number)

#Program 56
#Program to find LCM of to numbers
number1, number2 = map(int, input("Enter two numbers: ").split())

divisor = 2
lcm = 1
while number1 > 1 or number2 > 1:
    divided = False

    if number1 % divisor == 0:
        number1 //= divisor
        divided = True

    if number2 % divisor == 0:
        number2 //= divisor
        divided = True

    if divided:
        lcm *= divisor
    else:
        divisor += 1
print("The LCM of two numbers is:", lcm)

#Program 57
#Program to display first n term of fibbonaci series
number=int(input("Enter extend of fibbonaci series: "))
number1=0
number2=1

print("Fibbonaci series is: ")
if number > 1:
    print(number1)
    print(number2)
else:
    print(number1)
    
for i in range(number-2):
    number3=number1+number2
    number1=number2
    number2=number3
    print(number3)
    
#Program 58
#Program to find sum of n term of fibbonaci series
number=int(input("Enter a number: "))
start=0
next=1
sum=0
sum=sum+start
sum=sum+next
print("Sum of n terms ofFibbonaci series is: ")
for i in range(number-2):
    number3=start+next
    start=next
    next=number3
    sum=sum+number3

print(sum)

#Program 59
#Program to find the sum of the series 1 + 2 + 3 + ... + n.
number=int(input("Enter a number: "))
sum=0
for i in range(1,number+1):
    sum=sum+i
print("Sum of the series is: ",sum)

#Program 60
#Program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2.
number=int(input("Enter a number: "))
sum=0
for i in range(1,number+1):
    square=i**2
    sum=sum+square
print("The sum of series is: ",sum)"""





    

    
    
    
    
    
    
    
    
    
    

    
    

             

    


        

