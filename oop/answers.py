class players:
    def __init__(self, club, name):
        self.__club = club
        self.name = name
    
    def together(self):
        return f"{self.__club}: {self.name}"
    
    def get_club(self):
        return self.__club + "wow"
    
    def against_barca(self):
        return "Brilliant"
    
class contact_year(players):
    def __init__(self, club, name, contact):
        super().__init__(club, name)
        self.contact = contact

    def against_barca(self):
        return "poor"

bundesliga = contact_year("bayern", "kane", "3 years")
print(bundesliga.contact)

print(bundesliga.against_barca())
# print(bundesliga.club)
print(bundesliga.get_club())

print(bundesliga.together())

my_Player = players("Barca", "Pedri")

print(my_Player.against_barca())

print(my_Player.get_club())
print(my_Player.together())

players_arg = players("Inter Milan", "Lautaro")

print(players_arg.name)
print(players_arg.together())


# create student class that takes name and marks of 3 sub. as arguments in constructor, then create a method to print the average

class Student:
    def __init__(self, name, bangla, english, math):
        self.name = name
        self.bangla = bangla
        self.english = english
        self.math = math

    def average(self):
        print(self.name)
        mark = (self.bangla + self.english + self.math) / 3
        return mark
    
s1 = Student("Jawad", 34, 67, 78)

print(s1.average())

# create account class with 2 attributes - balance & account no. create methods for debits, credits and printing the balance --> solution

class Account:
    def __init__(self, bal, acc_no):
        self.balance =  bal
        self.account_no = acc_no

    def credit(self, amount):
        self.balance += amount
        return f"TK {amount} is credited"

    def debit(self, amount):
        self.balance -= amount
        return ("TK ", amount, "is debited")

    def total(self):
        print("Total balance is", self.balance)

account_man = Account(12000, "132412")
added = account_man.credit(500)
print(added)
account_man.total() 
