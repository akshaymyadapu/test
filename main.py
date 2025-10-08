Class Bank:
    def __init__(self, name,balance,pin,acno)
        self.name=name
        self.balance=0
        self.__pin=pin
        self.acno=acno
    def savingsaccount(self):
        return f"Account holder name is {self.name} and balance is {self.balance} this is savings account balance"
    def currentaccount(self):
        return f"Account holder name is {self.name} and balance is {self.balance} this is current account balance"
    def checkbalance(self,enteredpin):
        if enteredpin==self.__pin:
            return f"Your balance is {self.balance}"
        else:
            return "wrong pin"
    def forzeaccount(self,frozen):
        if frozen==self.__pin:
            self.balance>=100000000
            return "your account is frozen"
        else:
            return "your account is active"
    def deposit(self,amount):
        self.balance=self.balance+amount
        return f"your account is credited with {amount} and your new balance is {self.balance}"
    def withdraw(self,amount,enteredpin):
        if enteredpin==self.pin:
            if self.balance=self.balance-amount
                return f"your account is debited with {amount} and your new balance is {self.balance}"
            else:
                amount>self.balance
                return "insufficient balance"
