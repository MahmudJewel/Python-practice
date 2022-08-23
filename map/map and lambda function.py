cube = lambda x:x**3

def fibonacci(n):
    a,b=0,1
    arr=list(range(n))
    arr[0],arr[1]=a,b
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        arr[i]=c
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))