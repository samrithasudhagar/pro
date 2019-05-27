n,k=map(int,input().split())
l=list(map(int,input().split()))
c=int(input())
s=0
for i in range(len(l)):
    if i!=k:
        s=s+l[i]
if (s//2)>=c:
    print("Bon Appetit")
else:
    print((c-(s//2)))
