"""
Вариант 30
Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
Добавьте методы для вычисления процентных начислений и снятия денег.
"""

class Bank:
    def __init__(self, balance=0, interest_rate=0):
       
        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
       
        return self.balance * (self.interest_rate / 100)

    def withdraw(self, amount):
       
        if amount > self.balance:
            return False  
        self.balance -= amount
        return True

    def __str__(self):
        return f"Баланс: {self.balance}, Процентная ставка: {self.interest_rate}%"


if name == "__main__":
 
    account = Bank(1000, 5)

    print(account) 

  
    interest = account.calculate_interest()
    print(f"Процентные начисления: {interest}")  

   
    success = account.withdraw(500)
    if success:
        print("Снятие прошло успешно.")
    else:
        print("Недостаточно средств.")

    print(account)  
