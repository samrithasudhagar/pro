n=int(input())
k=[]
for i in range(100):
    if n==2**i:
        print("0")
        break
    else:
        t=abs(2**i-n)
        k.append(t)
print(min(k))
