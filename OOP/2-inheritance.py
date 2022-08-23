class A:
    def whoA(self):
        print("I'm A")
class B:
    def whoB(self):
        print("I'm B")

class C(A,B):  # Multiple inheritance
    def whoC(self):
        print("I'm C")

obj=C()
obj.whoA()
obj.whoB()
obj.whoC()