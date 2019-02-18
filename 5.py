n,a,b=map(int,input().split())

if n%2!=0:
    print("NO")
elif n==2 and a==1 and b==1:
    print("YES")
else:
    k=n//2
    for i in range(1,n):
        for j in range(1,n):
            if (a*i)+(b*j)==k and i==j:
                flag=0
                break
            else:
                flag=1
        if flag==0:
            break
    if flag==0:
        print("YES")
    else:
        print("NO")
