n=int(input())
l=list(map(int,input().split()))
l.sort()
p=[]
for i in l:
    p.append(1)
for i in range(len(l)):
    if i==0:
        p[0]=p[0]
    else:
        if l[i]==l[i-1]:
            p[i]=p[i-1]
        else:
            p[i]=p[i-1]+1
print(sum(p))
