a,b=map(str,input().split())
c=0
for i in a:
    for j in b:
        if i==j:
            c=c+1
if c>=2:
    print("yes")
else:
    print("no")
