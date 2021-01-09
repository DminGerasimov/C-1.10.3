import time

class EMoney:
    
    def __init__(self, account_number, account_value = 0):
        self.account_number = account_number
        self.account_value = account_value
        

    def get_account_value(self): #getter for account value
        return self.account_value

    def set_account_value(self, money): # setter for account value
        if money >= 0:
            self.account_value = money
            return True
        else:
            print("Account value can't be less zero!")
            return False

    def inc_account_value(self, money): # incremet of account value
        self.account_value += money

    def dec_account_value(self, money): # decremet of account value
        return True if self.set_account_value(self.account_value - money) else False


class Client(EMoney):
    
    def __init__(self, name, account_number, account_value = 0):# имя клиента, номер счета
        self.name = name
        self.account_number = account_number
        self.account_value = account_value

    def get_name(self):
        return self.name

    def set_name(self, name):
        if name:
            self.name = name
            return True
        else:
            print("Bad name")
            return False

    def transaction(self, mode, money): # mode = True - increment, else decrement - False
        return mode, int(time.time()), money