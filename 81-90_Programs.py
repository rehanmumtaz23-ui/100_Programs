"""#Program 81
#Program to find the sum and average of all elements in an array.
number=int(input("Enter leangth of List"))
numbers=[]
sum=0
for i in range(1,number+1):
    elements=int(input("Enter number: "))
    numbers.append(elements)
    

for i in range(len(numbers)):
    sum=sum+numbers[i]
    average=sum/number

print("Sum of the elements in array is: ",sum)
print("Average of the elements in array is: ",average)

#Program 82
#Program to find the largest and smallest element in an array.
number=int(input("Enter leangth of list: "))
numbers=[]
for i in range(1,number+1):
    element=int(input("Enter number: "))
    numbers.append(element)
    
    
largest=numbers[0]
smallest=numbers[0]
    
for i in range(len(numbers)):
    if numbers[i]>largest:
        largest=numbers[i]
    elif numbers[i]<smallest:
        smallest=numbers[i]

        

print("Largest element in list is: ",largest)
print("Smallest element in list is: ",smallest)

#Program 83
#Program to count the number of even and odd elements in an array
number=int(input("Enter leangth of list: "))
numbers=[]
even_count=0
odd_count=0

for i in range(1,number+1):
    element=int(input("Enter number: "))
    numbers.append(element)
    
for i in range(len(numbers)):
    if numbers[i]%2==0:
        even_count+=1
    else:
        odd_count+=1
        
        
print("Even numbers in list are:",even_count)
print("Odd numbers in list are:",odd_count)


#Program 84
#Program to search for an element in an array (linear search).
number=int(input("Enter leangth of list: "))
numbers=[]
num=int(input("Enter number you want to find: "))
is_found=False

for i in range(1,number+1):
    element=int(input("Enter number: "))
    numbers.append(element)

for i in range(len(numbers)):
    if numbers[i]==num:
        is_found=True
        
                
if is_found==True:
    print("Number Found")
else:
    print("Number does not exist in list")
    
    
#Program 85
#Program to reverse the elements of an array
number=int(input("Enter leangth of list: "))
numbers=[]
reverse=[]

for i in range(1,number+1):
    element=int(input("Enter number: "))
    numbers.append(element)
    
for i in range(len(numbers)-1,-1,-1):
    reverse.append(numbers[i])
    
print("Reversed list is: ",reverse)




#Program 86
#Program to find the second largest element in an array
numbers=[33,45,67,88,99]
largest=numbers[0]
second_largest=numbers[0]
for i in range(len(numbers)):
    if numbers[i]>largest:
        largest=numbers[i]

for i in range(len(numbers)):
    if numbers[i]<largest and numbers[i]>second_largest:
        second_largest=numbers[i]
                
print("Greatest number in list is: ",second_largest)

#Program 87
#Program to count the frequency of each element in an array
numbers=[33,33,333,33,3,33,333,33,3333333,33]
visited=[]
for i in range(len(numbers)):
    if numbers[i] not in visited:
        
        count=0
        for j in range(len(numbers)):
            if numbers[i]==numbers[j]:
                count+=1
        print(numbers[i],"appears",count,"times in list")
    visited.append(numbers[i])
    
#Program 88
#Program to remove duplicate elements from an array
numbers=[33,33,22,22,10,20,20,10,45,55]
visited=[]
for i in range(len(numbers)):
    if numbers[i] not in visited:
        visited.append(numbers[i])
 
 
print("Duplicates removed new list: ",visited)





#Program 89
#Program to sort an array in ascending order (bubble sort).
numbers=[2,35,7,98,1,32,44,7,8,9]
for i in range(len(numbers)):
    for j in range(len(numbers)-i-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

print("Sorted list: ",numbers)




#Program 90
#Program to merge two arrays into one.
num1=[1,2,3,4,5,]
num2=[6,7,8,9,10]
num3=[]
for i in range(len(num1)):
    num3.append(num1[i])

for j in range(len(num2)):
    num3.append(num2[j])
        
print("Two loops are merged",num3)"""
    







        