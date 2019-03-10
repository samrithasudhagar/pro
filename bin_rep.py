n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in range(n):
    a.append(bin(l[i]))
    b.append(l[i])
p=sorted(a,reverse=True)
s=sorted(b,reverse=True)
for i in range(len(a)-1):
    if p[i]==p[i+1]:
        if s[i+1]>s[i]:
            temp=s[i]
            s[i]=s[i+1]
            s[i+1]=temp
for i in range(len(s)):
    print(s[i])
