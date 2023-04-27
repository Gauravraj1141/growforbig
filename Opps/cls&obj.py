class Dairy:
    def __init__(self, name, balance):
        print("constructor called")
        self.name = name
        self.balance = balance

    def total(self):
        return self.balance


days = int(input("Enter Days: "))
total_bal = 0
for i in range(days*2):
    bal = float(input("Enter bal: "))
    Gaurav = Dairy('gauravj',bal)
    total_bal += float(Gaurav.total())
    print(round(total_bal))


