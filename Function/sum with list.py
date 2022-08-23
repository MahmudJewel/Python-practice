def sum(array,n):
    temp=0
    for i in range(n):
        temp+=array[i]

    return temp

n=int(input("Enter the size of array: "))
ar=list(range(n))
for i in range(n):
    ar[i]=int(input())

result=sum(ar,n)
print(result)
