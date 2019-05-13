n=int(input())
l=list(map(int,input().split()))
t=1
m=0
for i in range(1,n):
	if l[i]>l[i-1]:
		t=t+1
	else:
		if t>m:
			m=t
		t=1
if t>m:
	m=t
print(m)
		
