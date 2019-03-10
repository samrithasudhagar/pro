k=int(input())
a=[]
while k!=0:
    l=list(map(int,input().split()))
    for i in range(len(l)):
        a.append(l[i])
    k=k-1
k=sorted(a)
print(*k)
