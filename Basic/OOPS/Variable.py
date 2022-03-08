
a,b=40,45
class CheckVariables:
    a,b=90,50
    def add(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a']+globals()['b'])

ckl=CheckVariables()
ckl.add(200,100)

#constructor
class Constructor:
    def __init__(self):
        print("Constructor block")
    def method(self,name):
        print(name)
    def addition(self,a,b):
        print(a+b)
cons = Constructor()
cons.method("Chetan")
cons.addition(100,200)

#constructor example 2

class Emp:

    def __init__(self,empid,name,sal):
        self.empid = empid
        self.name  = name
        self.sal   = salk
    def display(self):
        print("EMP_ID :: {}".format(self.empid))
        print("NAME :: {}".format(self.name))
        print("SAL :: {}".format(self.sal))

emp1 = Emp(10,"Chetan",15000)
emp1.display()