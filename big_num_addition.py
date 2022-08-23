""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 16-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def reverse(s):
	str=''
	for i in s:
		str=i+str
	return str


def add(a1,a2):
	l1,l2=len(a1),len(a2)
	a1,a2=reverse(a1),reverse(a2)
	#print(a1,a2)
	if(l2>l1):
		a1,a2,l1,l2=a2,a1,l2,l1
	ans,result,rem,i,temp='',0,0,0,0
	for i in range(l2):
		sum=int(a1[i])+int(a2[i])+temp
		rem,result=sum%10,int(sum/10)
		ans+=str(rem)
		temp=result
	
	for j in range(i+1,l1):
		sum=int(a1[j])+temp
		rem,result=sum%10,int(sum/10)
		ans+=str(rem)
		temp=result

	if(temp>0):
		ans+=str(temp)
	ans=reverse(ans)
	return ans


while (1):
	a1,a2=input("Enter a num: ").strip(),input("Enter a num: ").strip()
	print(add(a1,a2))