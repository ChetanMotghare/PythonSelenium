class Oops:
    def first(self,name):
        print(name)
    def second(self,var1,var2):
        print(var1+var2)
c = Oops()
c.first("Chetan")
c.second(10,40)

class MyClass:
    def m1(self):
        print("Instance method")

    def m2(self):
        print(self ,"Static method no need to create an object")

ck = MyClass()
ck.m1
MyClass.m2(100)