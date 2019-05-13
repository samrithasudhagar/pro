m,n=map(int,input().split())
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
if m==a:
    if c==e:
        if c-a==b-m==d-f==e-m:
            if n==f:
                if b==d:
                    print("yes")
                else:
                    print("no")
            else:
                print("no")
        else:
            print("no")
    else:
        print("no")
else:
    print("no")
            
