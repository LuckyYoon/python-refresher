class account: 
    def __init__(self, balance, accID = "", name = ""):
        self.name = name
        self.balance = balance
        self.accID = accID
    
    def info(self):
        return (self.balance, self.accID, self.name)

    def withdraw(self, amount):
        if self.balance < amount or amount <= 0:
            ValueError("VALUE ERROR")
        else:
            self.balance = self.balance - amount
            print("NEW BALANCE: ", self.balance)
            return(self.balance)
        
    def deposit(self, amount):
        if amount <= 0:
            ValueError("VALUE ERROR")
        else:
            self.balance = self.balance + amount
            print("NEW BALANCE: ", self.balance)
            return(self.balance)

    def checkBalance(self):
        return(self.balance)