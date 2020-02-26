st=input("enter the string")
subst=input('enter the substring')
k=-1
c=0
for i in range(len(st)):
	k=st.find(subst,k+1)
	c+=1
print(c)
