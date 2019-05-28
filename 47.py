n,k=map(str,input().split())
k=int(k)
m=1111111111111111111111111111111111111111111111111111111111
if k==0:
    print(n)
else:
    for i in range(len(n)-1):
        for j in range(i+1,len(n)+1):
            for oo in range(k,100):
                jj=n[i:j]+("0"*oo)
                if int(jj)%int(n)==0:
                    if int(jj)<m:
                        m=int(jj)
    print(m)
