
t=int(input())
for test in range(t):
    n,k=map(int,input().strip().split())
    nos=list(map(int,input().strip().split()))
    count=[0]*(k+1)
    for x in nos:
        #that the difference between two elements can only ever be changed by a multiple of (k+1)
        #So, taking the given values mod(k+1), only those in the same residue class can be zero at the same time. 
        count[x%(k+1)]+=1
    if(max(count)>=n-1):
        print("YES")
    else:
        print("NO")