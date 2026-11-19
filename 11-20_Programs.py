"""
#Program 11
num=int(input("Enter a number:"))
if num%2==0:
    print("Number is even.")
else:
    print("Number is odd.")
    
#Program 12
num1=int(input("Enter a number:"))

if num1>0:
    print("Number is positive.")
elif num1<0:
    print("Number is negative.")
else:
    print("Number is zero.")
    
#Program 13
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
num3=int(input("Enter number3:"))

if num1>num2 and num1>num3:
    print("Number1 is largest.",num1)
elif num2>num1 and num2>num3:
    print("Number2 is largest.",num2)
else:
    print("Number3 is largest.",num3)
    
#Program 14
num4=int(input("Enter number1:"))
num5=int(input("Enter number2:"))
num6=int(input("Enter number3:"))

if num4<num5 and num4<num6:
    print("The smallest number is:",num4)
elif num5<num4 and num5<num6:
    print("The smallest number is:",num5)
else:
    print("The smallest number is:",num6)
    
#Program 15
year=int(input("Enter year:"))

if year%400==0:
    print("The entered year is a leap year.")
elif year%100==0:
    print("The entered year is not a leap year.")
elif year%4==0:
    print("The entered year is a leap year.")
else:
    print("The entered year is not a leap year.")
    
#Program 16
character=input("Enter a character:")
vowel=['a','e','i','o','u']
consonant=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

if character.lower() in vowel:
    print("The entered character is vowel.")
elif character.lower() in consonant:
    print("The entered character is consonant.")
else:
    print("Enter an alphabet.")
    
#Program 17
character=input("Enter a character:")
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
if character in alphabet:
    print("The entered character is an alphabet.")
else:
    print("The entered character is a special symbol.")
    
#Program 18
marks=int(input("Enter your marks:"))

if marks<0 or marks>100:
    print("Enter a valid number.")
elif marks>90:
    print("You are awarded with grade A+.")
elif marks>80:
    print("You are awarded with grade A")
elif marks>60:
    print("You are awarded with grade B.")
elif marks>50:
    print("You failed.")
else:
    print("You failed.")
    
#Program 19
number=int(input("Enter a number:"))

if number%3==0 and number%5==0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")
    
#Program 20
age=int(input("Enter the age:"))
if age>=18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")
"""