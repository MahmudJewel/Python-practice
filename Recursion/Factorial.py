def fact(n):
    if(n==1):
        print(n)
        return n
    else:
        print(n)
        return (n*fact(n-1))

n=int(input("Enter a number: "))
result=fact(n)
print(result)