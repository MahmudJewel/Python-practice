""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 16-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



m1,m2=input("Enter a num: "),input("Enter a num: ")
l1,l2=len(m1),len(m2)
sum,temp1,temp2=0,1,1
for j in range(l2-1,-1,-1):
	b=int(m2[j])*temp2
	#print(b)
	temp2*=10
	for i in range(l1-1,-1,-1):
		a=int(m1[i])
		sum=sum+a*b*temp1
		temp1*=10

print(sum)
