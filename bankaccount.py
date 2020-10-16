class Person:
    def __init__(self, name, age, profesi):
        self.name = name
        self.age = age
        self.profesi = profesi
    
    def print_status(self):
        pass


class BankAccount(Person):
    def __init__(self, name, age, profesi, id):
        super().__init__(name, age, profesi)
        self.id = id
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def print_balance(self):
        return self.balance

    def print_status(self):
        print(
            "Id : "+str(self.id)+"\nName : "+self.name+"\nAge: "+str(self.age)+"\nProfesi: "+self.profesi+"\nSaldo: "+str(self.balance)
        )


account = BankAccount("Giofanny Mowoka", 23, "IT Support", 1)
account.deposit(2000)
account.withdraw(150)
account.deposit(2000)
account.withdraw(1200)
account.print_status()
