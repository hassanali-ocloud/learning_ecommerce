class Rectangle:
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
    
    def area(self):
        return self.len * self.wid
    def perimeter(self):
        return 2*(self.len + self.wid)

# obj = Rectangle(5,5)
# print(obj.area())
# print(obj.perimeter())

class BankAcc:
    def __init__(self, balance) -> None:
        self.balance = balance
        
    def deposit(self, amount) -> None:
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount) ->  None:
        if (self.balance-amount > 0):
            self.balance = self.balance - amount
            return self.balance
        else:
            return None
    
    def showMeBalance(self) -> None:
        return self.balance

acc = BankAcc(200)
acc.withdraw(10)
acc.deposit(100)
print("Balance: ", acc.showMeBalance())
