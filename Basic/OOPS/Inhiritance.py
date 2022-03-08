#single inhiritance

class A:
    a,b=10,20
    def add(self):
        print(self.a+self.b)

class B(A):
    a,b=120,240
    def sub(self):
        print(self.a-self.b)

obj1=B()
obj1.add()
obj1.sub()

#multilevel
print(10*"*","Multilevel Inhiritance",10*"*")
class C(A):
    a,b=6,34
    def mul(self):
        print(self.a * self.b)

obj2=C()
obj2.add()
obj2.mul()

class D():
    a,b=90,45
    def name(self):
        print(self.a,self.b)

class E(A,D):
    a,b=78,9
    def div(self):
        print(self.a/self.b)

obj3=E()
obj3.name()
obj3.add()
obj3.div()

#overriding
print("*****Overriding******")

class Bank():
    def rateOfInterest(self):
        return 4
class iciciBank(Bank):
    def rateOfInterest(self):
        return 9
class yesBank(Bank):
    def rateOfInterest(self):
        return  12
interest=iciciBank()
print(interest.rateOfInterest())
interest=yesBank()
print(interest.rateOfInterest())

print("*****Overloding******")
class Calculation:
    def calculate(self,a=0,b=0,c=0):
        print(a+b+c)
     
cal=Calculation()
cal.calculate()
cal.calculate(10,30)
cal.calculate(45,56,98)
