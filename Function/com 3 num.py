def comparison(a,b,c):
    if (a > b and a > c):
        print(c, "is greater among", a, b, c)
    elif (b > a and b > c):
        print(b, "is greater among", a, b, c)
    else:
        print(c, "is greater among ", a, b, c)

n1=int(input())
n2=int(input())
n3=int(input())
comparison(n1,n2,n3)
