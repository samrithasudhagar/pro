n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
t=min(l)
d=len(t)
for i in range(1,d+1):
    for j in l:
        a=t[0:i]
        if a==j[0:i]:
            x=a
print(x)
