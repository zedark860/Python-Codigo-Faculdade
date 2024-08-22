
class BankAccount:
    def __init__(self, account_number: int, balance: float) -> None:
        self.__account_number = account_number
        self.__balance = balance
        
        
    def deposit(self, value: float) -> None:
        self.__balance += value
        
        
    def withdraw(self, value: float) -> None:
        if not (value <= self.__balance):
            raise Exception("O valor do saque é maior do que o saldo na conta!")
        
        self.__balance -= value
       
        
    def balance_display(self) -> None:
        print(f"Conta: {self.__account_number}\nSeu saldo atual é {self.__balance}")
        
        
if __name__ == "__main__":
    try:
        bankAccount: BankAccount = BankAccount(1234, 100.0)
        
        bankAccount.balance_display()
        
        bankAccount.withdraw(50.0)
        
        bankAccount.balance_display()
        
        bankAccount.withdraw(50.0)
        
        bankAccount.balance_display()
        
        bankAccount.deposit(100.0)
        
        bankAccount.balance_display()
    except Exception as e:
        print(e)
        