s=input("enter the string")
sub=input("enter the substring")
c=0
for i in range(0,len(s)):
	if sub==s[i:i+len(sub)]:
		c=c+1
print(c)
