class A:
    def A(self):
        print("I'm A")

class B:
    def A(self):
        print("I'm B's A")
    def B(self):
        print("I'm B")

#multiple inheritance
class C(A,B):  # Priority ==> Inherit left to right sequence ==> A > B
    def C(self):
        print("I'm C")
#multiple inheritance
class D(B,A):  # Priority ==> Inherit left to right sequence ==> B > A
    def D(self):
        print("I'm D")
c=C()
d=D()
c.A()    #call A==> A()
d.A()    #call B==> A()
