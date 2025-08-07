def mostCompetative(nums,k):
    stack=[]
    remove=len(nums)-k
    for num in nums:
        while stack and remove>0 and stack[-1]>num:
            stack.pop()
            remove=-1
        stack.append(num)
    return stack[:k]

n,k=map(int,input().split())
nums=list(map(int,input().split()))

result=mostCompetative(nums,k)
print(*result)