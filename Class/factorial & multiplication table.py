class mfun:
    def __init__(self,n):
        self.n=n

    def multiple(self):
        print("The multiplication table of",n,"is:")
        for i in range(1,11):
            print(i,"X",self.n,"=",i*self.n)

    def factorial(self):
        temp=int(self.n/2)+1
        print("The factorial of",n,"is")
        for i in range(1,temp):
            if(int(self.n%i)==0):
                print(i)
        print(self.n)

while(1) :
    n=int(input("Enter a number: "))
    ob1 = mfun(n)
    ob1.multiple()
    ob1.factorial()

