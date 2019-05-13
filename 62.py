n=input()
kk=""
m=0
oo=""
ll=""
for i in range(len(n)-1):
    for j in range(i+1,len(n)+1):
        kk=n[i:j]
       
        if kk==kk[::-1]:
            if len(kk)>m:
                
                m=len(kk)
                oo==kk
                ll=n[0:i]+n[j:]
po=len(ll)
                
print(po)
        
