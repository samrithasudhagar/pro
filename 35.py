s=input()
a=[]
kk=1000000
k=1
p=1
while k<len(s)+1:
    a=[]
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)+1):
            if len(s[i:j])==k:
                a.append(s[i:j])
    for ii in s:
        c=0
        for jj in a:
            if ii in jj:
                c=c+1
        if c==len(a):
            p=0
            print(k)
            break
    if p==0:
        break
        
    k=k+1
