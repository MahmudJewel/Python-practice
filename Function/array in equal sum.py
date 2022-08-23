def sequal(arr,n,m):
    for i in range(n-1):
        if(arr[i]+arr[i+1]==m):
            print(arr[i],arr[i+1])
            break



m=int(input("Enter the sum: "))
n=int(input("Enter array length: "))
print("Enter the value of array")
arr=list(range(n))
for i in range(n):
    arr[i]=int(input())
sequal(arr,n,m)
