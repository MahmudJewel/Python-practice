#import self as self


class employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def dishSalary(self):
        print("Name:", self.name, "\nSalary: ",self.salary)
    def increment(self):
        print("Name:", self.name,"\nSalary:",self.salary+self.salary*0.2)

emp1=employee("Jahid",10000)
emp1.dishSalary()
emp1.increment()
