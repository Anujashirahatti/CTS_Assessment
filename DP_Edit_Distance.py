#Edit distance
#Take two strings start and target, you need to determine the minimum number of operations required to convert the string start into the string target. The operations you can use are:
#Insert a character: Add any single character at any position in the string.
#Delete a character: Remove any single character from the string.
#Replace a character: Change any single character in the string to another character.
#The goal is to transform start into target using the fewest number of these operations.
#Input Format:The first line of input contains a string start (1≤ length of start ≤ 1000)
def edit_distance(start,target):
    m=len(start) #Number of rows
    n=len(target) #Number of Col
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0]=i
    for j in range(n+1):
        dp[0][j]=j
    for i in range(m+1):
        for j in range(n+1):
            if start[i-1]==target[j-1]:# if char mathes and if char are differ then !=
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                #dp[i-1][j] +1 for delete 
                #dp[i][j-1]+1 for insert
                #dp[i-1][j-1]+1 for replace
    return dp[m][n]
start=input().strip()
target=input().strip()
print(edit_distance(start,target))