n=int(input())
a_list=list(range(n))
for i in range(n):
    a_list[i]=int(input())
    #print(i)

sum=0;
for i in range(n):
    sum+=a_list[i]

avg=sum/n
print("The sum is ",sum,"\nThe average is ",avg)