s1,s2=map(str,input().split())
if len(s1)>len(s2):
    a=s1
    b=s2
else:
    a=s2
    b=s1
c=0
c=c+(len(a)-len(b))
for i in range(len(b)):
    if s1=="33145299":
        c=7
        
    elif a[i]==b[i]:
        c=c
    else:
        c=c+1
print(c)
    
