"""#Program 41
#Program to check if the number is palindrome

number=int(input("Enter a number: "))
reverse=0
original=number
while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
    
    
if original==reverse:
    print("Yes the number is palindrome")
else:
    print("No the number is not a palindrome")
    
#Program 42
#Program to replace all the 0 in a number with 5
number=int(input("Enter a number: "))
new_number=0
while number>0:
    digit=number%10
    number=number//10
    
    if digit==0:
        digit=5
       
    new_number=new_number*10+digit


reverse=0
while new_number>0:
    digit=new_number%10
    new_number=new_number//10
    reverse=reverse*10+digit
    
print("The number after replacement is: ",reverse)

#Program #43
#Program to find the sum of first and last digit of a number
number=int(input("Enter a number: "))
num=[]
while number>0:
    digit=number%10
    number=number//10
    num.append(digit)

sum=num[0]+num[-1]
print("The sum of 1st and last digit of a number is: ",sum)


#Program 44
#Check number weather number is prime or not
number=int(input("Enter a number: "))
if number%2==0:
    print("Number is a prime number")
else:
    print("Number is not prime")
    
#Program 45
#Prime numbers from 1 to n   
n=int(input("Enter the range: "))
for i in range(n):
    if i%2!=0:
        print("Prime numbers from 1 to n are: ",i)
        
#Program 46
#Program to print first n prime numbers
num=int(input("Enter the range: "))
n=int(input("Enter how many prime numbers you want to print: "))
count=0

for i in range(num):
    if i%2!=0:
        print("Prime numbers are: ",i)
        count +=1
        
    if  count==n:
        break
        

#Program no 47
#program to check weather number is an armstrong or not
number=int(input('Enter your number: '))
count=0
num1=[]
power=[]
original=number
while number >0:
	digit=number%10
	number=number//10
	count+=1
	num1.append(digit)

for i in num1:
	multiply=i**count
	power.append(multiply)
	total=sum(power)
	

if total==original:
	print('The entered number is armstrong number')
else:
		print('The entered number is not armstrong number')
		
#Program no 48
#Armstrong numbers from 1 to n
number=int(input('Enter a number: '))
print('The armstrong numbers are: ')
temp=i
original=i
for i in range(1,number+1):
	count=0
while i>0:
	temp=i%10
	i=i//10
	count+=1
	print(count)
	
#Program 49
#Program to check weather a number is a perfect number
number=int(input('Enter a number: '))
total=[]
for i in range(1,number):
    if number%i==0:
        total.append(i)
        
add=sum(total)
    
if add==number:
    print("Number is a perfect number")
else:
    print("Number is not a perfect number")
    

#Program 50
#Program to check weather number is a strong number
number=int(input("Enter a number"))
original=number
total=0
#First extract the number
while number>0:
    digit=number%10
    number=number//10
    number2=1
    for i in range(1,digit+1):
        number2=number2*i
        
    
    total+=number2
        
if total==original:
    print("Number is a strong number.")
else:
    print("Number is not a strong number")"""
	