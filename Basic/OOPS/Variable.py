a,b=40,45
class CheckVariables:
    a=90
    b=60
    def add(self,a,b):
        print("Addition of local var :: ",a+b)
        print("Addition of class var :: ",self.a+self.b)
        print("Addition of global var :: ",globals()['a']+globals()['b'])

ckl=CheckVariables
ckl.add(78,40,76)