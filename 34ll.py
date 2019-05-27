n=int(input())
s=""
a=[]
for i in range(0,2**n):
    s=""
    pp=len(bin(i)[2:])
    if pp<n:
        s=s+"0"*(n-pp)+str(bin(i)[2:])
    else:
        s=s+str(bin(i)[2:])
    a.append([s,s.count("1")])
a.sort(key=lambda x:x[1])
for i in range(len(a)):
    print(a[i][0])
