class ATM(object):

    def __init__(self, money, cardNum, pin):
        self.money=money
        self.cardNum=cardNum
        self.pin=pin
    def withdraw(self, amount):
        self.money -= amount
        print('you have withdrawn', amount)
        print('your balance is', self.money)
    def deposit(self, amountD):
        self.money += amountD
        print('you have diposited', amountD)
        print('your balance is', self.money)

atm = ATM(100, 45435434436, 5656)
atm.withdraw(20)
atm.deposit(20)
