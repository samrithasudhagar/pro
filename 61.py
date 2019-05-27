a=input()
c=input()
s=""
l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range(len(a)):
    k=l.index(a[i])
    p=l.index(c[i])
    s=s+l[(k+p)%26+1]
print(s)
