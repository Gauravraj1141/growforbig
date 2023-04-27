
class Prac:
    globalvar = "globe"
    def __init__(self):
        self.privatevar = "private"

     # we can access this globalvar from this classmethod
    @classmethod
    def my_func(cls):
        cls.raj = "raja"
        print("it is class method so we can call it by class name ")
        print(cls.globalvar,cls.raj)

    def newfun(self):
        print(self)
        print("this is instance method  we can call it by instance/object and class also")



Gaurav  = Prac()
ram = Prac()
# so this global variable changed only for this Gaurav instance
Gaurav.globalvar = "gauravglobal"
print(Gaurav.globalvar)  # changeglobal
print(ram.globalvar)  # globe
print(Prac.globalvar)  # globe

ram.globalvar = "ramglobal"
print(ram.globalvar)

Gaurav.my_func()
# we can access this varialbe from this cls method
print(Gaurav.raj)

# we can call this function by class name
Prac.my_func()  # globe raja
# here we should give the value of self when we call it by class
Prac.newfun(self="gaurav")