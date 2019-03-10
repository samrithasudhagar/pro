n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(n):
    for j in range(0,i):
        if a[j]<a[i]:
            l.append(a[j])
print(sum(l))
