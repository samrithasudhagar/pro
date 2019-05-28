n=int(input())
l=list(map(int,input().split()))
c=1
t=[]
for i in range(n):
    for j in range(i,n-1):
        if (l[j]>0 and l[j+1]<0) or (l[j]<0 and l[j+1]>0):
            c+=1
        else:
            break
    t.append(c)
            
    c=1
print(*t)
