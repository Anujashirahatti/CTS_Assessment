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

