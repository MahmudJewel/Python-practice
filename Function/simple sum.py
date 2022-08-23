def sum(n):
    temp=0
    for i in range(1,n+1):
        temp+=i

    return temp

#n=int(input("Enter the size of array: "))

for i in range(10):
    n=int(input("Enter the size of array: "))
    result = sum(n)
    print(result)

