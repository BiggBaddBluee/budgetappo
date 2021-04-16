
budgetAmount = 50000
print(f"Your budget is {budgetAmount}")

class Budget():

    def  __init__(self, category, amount):
        self.category = category
        self.amount = amount

    '''
    methods for the budget object
    '''
    def withdraw (self):
        print(f'You just withdrew {self.amount} for {self.category}')
        withdrawAmount = budgetAmount - self.amount #assigning the formular of withdraw to the variable withdrawAmount
        print(f"your budget balance is now {withdrawAmount}")
        
    def deposit (self):
        print(f'You just deposited {self.amount} for {self.category}')
        depositAmount = budgetAmount + self.amount #assigning the formular of deposit to the variable depositAmount
        print(f"your budget balance is now {depositAmount}")
    

    def transfer (self, newBudget):
        self.newBudget = newBudget
        print(f"You just transferred {self.amount} from {self.category} budget to {self.newBudget} budget")

    def checkBalance (self):
        print(f"Your balance for {self.category} budget is {self.amount}")
        print(f"Your total budget is {budgetAmount}")

'''
objects listed
'''
Budget1 = Budget("food", 1000)
Budget2 = Budget("Entertainment", 6000)
Budget3 = Budget("Clothing", 7000) #category and amount to be transferred from
Budget4 = Budget("Luxury", 3000)
 
'''
instantiating
'''
Budget1.withdraw()
Budget2.deposit()
Budget3.transfer("Entertainment") #where the amount is transferred to from line 38
Budget4.checkBalance()
