import math
l=list(map(int,input().split()))
C=50
H=30
e=[]
for i in l:
	q=math.pow((2*C*i)/H,0.5)
	e.append(q)
print(e)

