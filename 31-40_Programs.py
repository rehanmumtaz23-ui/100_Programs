"""#Program 31
num=int(input("Enter a number:"))
count=0
for i in range(1,num):
    if(i%3==0):
        count+=1
    
print("Numbers divisible by 3 from 1 to",num,"are",count)

#Program 32
num1=int(input("Enter a number"))
for i in range(1,num1):
    if(i%3==0|i%5==0):
        print("Numbers divisible by 3 or 5 are",i)
        
#Program 33
num=int(input("Enter a number:"))
count=0
while num>0:
    digit=num%10
    num=num//10
    count+=1

print("Number of digits in number are:",count)


#Progtam 34
num1=int(input("Enter a number:"))
while num1>0:
    digit=num1%10
    num1=num1//10
    print("Digits of the number are:",digit)
    
    
#Program 35
#Program to find sum of all digits of number n
number=int(input("Enter a number:"))
sum=0

while number>0:
    digit=number%10
    number=number//10
    sum+=digit

print("Sum of all digits in a number n are:",sum,"😭")
    
#Program 36
#Program to find product of all digits of a number n
num=int(input("Enter a number:"))
product=1
while num>0:
    digit=num%10
    num=num//10
    product*=digit
    
print("Product of all digits in a number n are:",product,"😭")

#Program 37
#Program to reverse a number n
number=int(input("Enter a number:"))
reverse=0
while number>0:
    digit=number%10
    reverse=digit
    number=number//10
    print("Number after reversing is:",reverse)
    
#Program 38
#Program for largest digit in a number n
number=int(input("Enter a number:"))
max=[]
greatest=0
while number>0:
    digit=number%10
    number=number//10
    max.append(digit)
    max.sort()

for i in max:
    greatest=i
    
    
print("Greatest digit in the number is:",greatest)

#Program 39
#Program to find smallest digit in a number
number=int(input("Enter a number:"))
list=[]
smallest=0
while number>0:
    digit=number%10
    number=number//10
    list.append(digit)
    list.sort()
    
print("The smallest digit in the number is: ",list[0])

#Program 40
#Program to find number of odd digit and even digits in a number n
number=int(input("Enter a number: "))
even=0
odd=0

while number>0:
    digit=number%10
    number=number//10
    if digit%2==0:
        even +=1
    else:
        odd +=1
        
print("Even digits in a number n are:",even)
print("Odd digits in a number n are:",odd) """


     


    
          
    
    
    
    
    

 
    
    

