n,t=map(int,input().split())
l=list(map(int,input().split()))
c=0
mm=0
for i in l:
    mm=mm+86400-i
    if mm<=t:
        c=c+1
print(c)
        
