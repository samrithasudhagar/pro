s=input()
if s==s[::-1]:
    print("yes")
else:
    k=s.strip("0")
    if k==k[::-1]:
        print("yes")
   
    else:
        k=s.lstrip("0")
        if k==k[::-1]:
            print("yes")
        else:
            print("no")
