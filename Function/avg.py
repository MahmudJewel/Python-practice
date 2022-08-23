def avg(ml,n):
    sum=0
    for i in range(n):
        sum+=ml[i]
    return sum/n

#main blocks
n = int(input("Enter the size of List: "))
a_list = list(range(n))
for i in range(n):
    a_list[i] = int(input())

result=avg(a_list,n)
print("The Average is ",result)

