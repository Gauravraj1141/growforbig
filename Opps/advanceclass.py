class School:
    teacher = 4

    def all_staf(self):
        self.teacher = "44"
        print(self.teacher)

    @classmethod
    def clsmethod(cls):
        cls.teacher = 55
        print(cls.teacher)


Gaurav = School()
print(School.teacher)
# here i call this all_staf function by class name and give the instance in it
School.all_staf(self=Gaurav)  #44
