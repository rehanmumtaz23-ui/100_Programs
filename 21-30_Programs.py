"""#Program 21
n=int(input("Enter the range of number:"))
for i in range(n):
    print(i)
    
#Program 22
n1=int(input("Enter the range of number:"))
for i in range(n1):
    n1=n1-1
    print(n1)
    
#Program 23
n2=int(input("Enter the range:"))
print("The even number between 1 to n are:")
for i in range(n2):
    if i%2==0:
        print(i)
        
#Program 24
n3=int(input("Enter the range of number:"))
print("The odd numbers between 1 to n are:")
for i in range(n3):
    if i%2!=0:
        print(i)
        
#Program 25
n4=int(input("Enter the range of number:"))
sum=0
for i in range(n4):
    sum+=i
    
print(sum)


#Program 26
n5=int(input("Enter the range of number:"))
sum=0
for i in range(n5):
    if i%2==0:
        sum+=i
print(sum)

#Program 27
n6=int(input("Enter the range of number:"))
sum=0
for i in range(n6):
    if i%2!=0:
        sum+=i
print(sum)

#Program 28
num=int(input("Enter a number:"))
fact=1
for i in range(num,0,-1):
    fact*=i
print("Factorial of number is:",fact)

#Program 29
num=int(input("Enter a number:"))
last=11
table=1

for i in range(last):
    print(num,"*",i,"=",num*i)
    
#Program 30
num=int(input("Enter a number to find multiples:"))
for i in range(1,num):
    if(num%i==0):
     print("Multiples of",num,"are",num/i)"""
     