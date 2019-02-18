from itertools import combinations
s,n=map(str,input().split())
n=int(n)
s=list(s)
p=list(combinations(s,len(s)-n))
d=min(p)
l=""
for i in d:
    l=l+i
    
print(l)
