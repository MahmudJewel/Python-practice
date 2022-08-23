print("Enter three numbers")
a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print(c,"is greater among",a,b,c)
elif(b>a and b>c):
    print(b,"is greater among",a,b,c)
else:
    print(c,"is greater among ",a,b,c)