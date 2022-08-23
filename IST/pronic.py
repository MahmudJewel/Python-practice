def pronic(n):
	for m in range(1, n):
		if (m * (m+1) == n):
			result.append(n)


str1=input().strip()
l=len(str1)
temp=0
result=[]
str2=''
for i in range(l):
    a,b=0,1+i
    for j in range(l-i):
        n=int((str1[a:b]))
        pronic(n)
        a,b=a+1,b+1
        temp+=1

sett=set(result)

if(len(sett)==0):
	print('-1')

else:
	ab=""
	for i in sorted(sett):
		ab=ab+str(i)+','
	print(ab.strip(','))
