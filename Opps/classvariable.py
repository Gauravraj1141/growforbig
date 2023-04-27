
class Prac:
    globalvar = "globe"
    def __init__(self):
        self.privatevar = "private"

     # we can access this globalvar from this classmethod
    @classmethod
    def my_func(cls):
        cls.raj = "raja"
        print(cls.globalvar,cls.raj)



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