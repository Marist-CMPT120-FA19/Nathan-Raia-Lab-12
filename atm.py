#Nathan Raia

class Account:

    def __init__(self , id , pin , savings , checking):
        self.ID = id
        self.PIN = pin
        self.savings = int(savings)
        self.checking = int(checking)
        
    def getID(self):
        return self.ID
        
    def getPIN(self):
        return self.PIN
        
    def getSavings(self):
        return self.savings
        
    def getChecking(self):
        return self.checking
        
    def withdraw(self , account , amm):
        if account == "savings":
            self.savings = self.savings - int(amm)
        elif account == "checking":
            self.checking = self.checking - int(amm)

    def transfer(self , toAcc , amm):
        if toAcc == "savings":
            self.savings = self.savings + int(amm)
            self.checking = self.checking - int(amm)
        elif toAcc == "checking":
            self.savings = self.savings - int(amm)
            self.checking = self.checking + int(amm)
            
    def toString(self):
        return str(str(self.ID) + "\t" + str(self.PIN) + "\t" + str(self.savings) + "\t" + str(self.checking))
        
def checkCredentials(id , pin):
    accountsFile = open("accounts.txt" , "r")
    for i in accountsFile:
        a = createAccount(i.split("\t"))
        if id == a.getID():
            if pin == a.getPIN():
                accountsFile.close()
                return True        
                
def createAccount(info):
    return Account(info[0] , info[1] , info[2] , info[3])
    
def accountMenu(acc):    
    
    b = True
    while b:
        print("Your current balances are... \n Savings Account: $" , acc.getSavings() , "\n Checking Account: $" , acc.getChecking())
        print("\nWhat would you like to do? \n1) Withdraw cash \n2) Transfer funds \n3) Quit")
        action = int(input("Answer with 1, 2, or 3: "))
        if action == 1:
            ammount = int(input("How much cash would you like to withdraw: "))
            account = input("From which account: ")
            if account.lower() == "savings":
                if ammount <= acc.getSavings():
                    acc.withdraw(account.lower() , ammount)
                    print("Your transaction was completed... \n")
                else:
                    print("The requested ammount of money was more than there is in the account.")
            elif account.lower() == "checking":
                if ammount <= acc.getChecking():
                    acc.withdraw(account.lower() , ammount)
                    print("Your transaction was completed... \n")
                else:
                    print("The requested ammount of money was more than there is in the account.")
                    print("Sending you back to the top... \n")
        elif action == 2:
            ammount = int(input("How much money would you like to transfer: "))
            account = input("From which account: ")
            if account.lower() == "savings":
                if ammount <= acc.getSavings():
                    acc.transfer(account.lower() , ammount)
                    print("Your transaction was completed... \n")
                else:
                    print("The requested ammount of money was more than there is in the account.")
            elif account.lower() == "checking":
                if ammount <= acc.getChecking():
                    acc.transfer(acc.lower() , ammount)
                    print("Your transaction was completed... \n")
                else:
                    print("The requested ammount of money was more than there is in the account.")
                    print("Sending you back to the top... \n")
        elif action == 3:
            b = False
        else:
            print("That was an invalid selection! \n")
            print("Sending you back to the top... \n")
            
    accountsFile = open("accounts.txt" , "r")
    counter = -1
    newFile = []
    for i in accountsFile:
        counter += 1
        newFile = newFile + [i]
        if i.split("\t")[0] == acc.getID():
            newFile[counter] = acc.toString()
        else:
            newFile[counter] = i
    accountsFile.close()
    accountsFile = open("accounts.txt" , "w")
    for i in range(counter+1):
        accountsFile.write(newFile[i])
        if i == 0:
            accountsFile.write("\n")
    accountsFile.close()
            
def main():
    
    b = True
    while b:
        id = input("Enter your account ID: ")
        pin = input("Enter your corresponding PIN: ")
        
        if checkCredentials(id , pin):
            b = False
            accountsFile = open("accounts.txt" , "r")
            for i in accountsFile:
                a = createAccount(i.split("\t"))
                if id == a.getID():
                    if id == a.getPIN():
                        accountMenu(a)
        else:
            print("Invalid Credentials! \nPlease try again... \n")
    
if __name__ == '__main__':
    main()
