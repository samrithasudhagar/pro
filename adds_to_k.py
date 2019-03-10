n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(i,n):
        if l[i]+l[j]==k:
            flag=1
            break
        else:
            flag=0
    if flag==1:
        break
if flag==1:
    print("yes")
else:
    print("no")
