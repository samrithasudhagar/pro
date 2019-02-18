n=int(input())
k=[]
for i in range(100):
    
        t=abs(2**i-n)
        k.append(t)
print(min(k))
    
