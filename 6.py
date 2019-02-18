n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if l[i]<l[j]:
                if l[j]<l[k]:
                    if i<j:
                        if j<k:
                            c=c+1
                
print(c)
