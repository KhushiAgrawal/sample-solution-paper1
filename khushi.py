l=list(map(int,input().split()))
E=[ ]
for i in l:
	f=1
	while i!=0:
		f=f*i
		i=i-1
	E.append(f)
print(E)
