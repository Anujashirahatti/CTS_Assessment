#TwoFloatingPoints with Two decimal Places
a,b=map(float,input().split())
result=a+b
print("{:.2f}".format(result))


#Fibonacci Series
n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b

#Binary Conversion
n=int(input())
print(bin(n)[2:])

#integer and float
a=int(input())
b=int(input())
print(a//b) #Returns Interger Vlaue
print(a/b)  #Returns Floating Vlaue

#Prime Number
def is_prime(n):
    if(n<=1):
        return("Not Prime")
    elif (n==0):
        return("Prime Number")
    else:
        for i in range(2,n):
            if n%i==0:
                return("Not Prime")
        print("Prime")
        
n=int(input())
is_prime(n)

#Alternative
def is_prime(n):
    if(n==1):
        print("Not Prime")
        return
    for i in range(2,int(n**0.5)+1):
        if (n%i==0):
            print("Not Prime")
            return
    print("Prime")
        
n=int(input())
is_prime(n)

#Freq Count
n=int(input())
nums=list(map(int,input().split()))
freq={}
for num in nums:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key in sorted(freq):
    print(f"{key}: {freq[key]}")

#Take a input as float and interger typecast it 
f,i=input().split()
f=float(f)
i=int(i)
r=f+i
print(r)

#Take two input values a,b print sum , difference and product of the values
a=int(input())
b=int(input())
sum=a+b
difference=a-b
product=a*b
print(sum)
print(difference)
print(product)

# Write a program to print age 
age=int(input())
if (age>=18):
    print("Adult")
elif (age<18):
    print("Teen")
else:
    print("Either one of this")

#String A and B contain alphabets in upper case only Leftover-string
A=input().strip()
B=input().strip() #Strip Can be used as removes leading and trailing whitespace
result=''.join([char for char in A if char not in B])
print(result if result else "Empty")

#Matrix Daigonal Element to be swap 
n=int(input())
matrix=[list(map(int,input().split())) for _ in range(n)]
for i in range(n):
   matrix[i][i],matrix[i][n-i-1]=matrix[i][n-i-1],matrix[i][i]
   
for row in matrix:
    print(*row)







