n,q=map(int,input().split())
l=list(map(int,input().split()))
a=[]
while q!=0:
    s=0
    u,v=map(int,input().split())
    min=l[u-1]
    for i in range(u-1,v):
        if l[i]<min:
            min=l[i]
        if i==v-1:
            a.append(min)
    q=q-1
for i in range(0,len(a)):
    print(a[i])
