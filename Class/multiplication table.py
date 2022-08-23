class mtable:
    def __init__(self,n):
        self.n=n

    def dishplay(self):
        for i in range(1,11):
            print(i,'X',self.n,'=',i*self.n)

n=int(input("Enter the number: "))
obj=mtable(n)
obj.dishplay()

