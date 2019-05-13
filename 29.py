n=int(input())
c=0
j=[]
for i in range(1,n):
	r=0
	k=i
	while(i>0):
		s=i%10
		r=r+s
		i=i//10
	if k+r==n:
		c=c+1
		j.append(k)
print(c)
for q in j:
	print(q)
