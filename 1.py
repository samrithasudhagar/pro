n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
t=min(l)
d=len(t)
for i in range(1,d+1):
   
        a=t[0:i]
        if all(a==j[0:i] for j in l):
            x=a
print(x)
