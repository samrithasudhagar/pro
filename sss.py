n=int(input())
l=list(map(int,input().split()))
a_ha=0
b_ha=0
l.sort(reverse=True)
for i in l:
  m=a_ha+i
  if b_ha>m:
    a_ha=m
  else:
    a_ha=b_ha
    b_ha=m
print(a_ha,b_ha)
#i
