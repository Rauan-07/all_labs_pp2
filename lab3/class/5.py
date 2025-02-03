class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} внесено. Текущий баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} снято. Текущий баланс: {self.balance}")
        else:
            print("Недостаточно средств для снятия.")

owner_name = input("Введите имя владельца счета: ")
account = Account(owner_name, 0)  

while True:
    print("\nВыберите операцию:")
    print("1. Внести депозит")
    print("2. Снять деньги")
    print("3. Проверить баланс")
    print("4. Выйти")

    choice = input("Введите номер операции: ")

    if choice == '1':
        deposit_amount = float(input("Введите сумму депозита: "))
        account.deposit(deposit_amount)

    elif choice == '2':
        withdraw_amount = float(input("Введите сумму для снятия: "))
        account.withdraw(withdraw_amount)

    elif choice == '3':
        print(f"Текущий баланс: {account.balance}")

    elif choice == '4':
        print("Выход из программы.")
        break

    else:
        print("Неверный ввод. Пожалуйста, выберите правильную операцию.")
