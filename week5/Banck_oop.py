class Banck():
    __balance=25
    # def __init__(self,acc_number):
    #     self.acc_number=acc_number  
    def deposit(self,amount):
        self.__balance+=amount
        print("Deposited successfuly!")
    def withdraw(self):
        withd=int(input("Enter amount of money to withdraw: "))
        self.__balance-=withd
        print("Withdrawal success!")
    def display_balance(self):
        print("Your current balance is: ",self.__balance)
# acc=int(input("Enter ur account number: "))
print("1.Deposit\n2.Withdraw\n3.check_balance")
choice=int(input("Enter ur choice: "))
b1=Banck()
if choice==1:
   money=float(input("Enter amount u want to deposit: "))
   b1.deposit(money)
elif choice==2:
     money=float("Enter amount u want to withdraw: ")
     b1.withdraw(money)
elif choice==3:
    b1.display_balance()
