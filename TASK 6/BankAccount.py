class BankAccount:
    def __init__(self,account_no,balance):

        self.account_no= account_no
        self.balance= balance
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):        
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("insuficient balance")  
class SavingsAcount(BankAccount):
    def __init__(self,account_no,balance,interest_rate):
        super().__init__(account_no,balance)
        self.interest_rate=interest_rate 
    def calculate_interest(self):
        interest=self.balance+self.interest_rate/100
        return interest    

class CurrentAccount(BankAccount):
    def __init__(self, account_no,balance,minimum_balance):
        super().__init__(account_no,balance)
        self.minimum_balance=minimum_balance

    def withdraw(self, amount):
        if self.balance - amount>=self.minimum_balance:
            self.balance -=amount
        else:    
            print("Minimum balance")

savings  = SavingsAcount(100,10000,7)   
savings.deposit(2000)
print("saving balance:",savings.balance)
savings.withdraw(2500)
print("savings balance aftr withdraw:",savings.balance)    

print(savings.calculate_interest())

current=CurrentAccount(11,20000,4000)
current.deposit(5000)
print(current.balance)
current.withdraw(10000)
print(current.balance)
current.withdraw(11000)

#Employee Management
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.sal=salary
    def calculate_sal(self):
        return self.sal
class RegularEmployee(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name, salary)
        self.bonus=bonus
    def calculate_sal(self):
        return self.sal+self.bonus
class ContractEmployee(Employee):
    def __init__(self,name,salary,months):
        super().__init__(name, salary)
        self.months=months
    def calculate_sal(self):
        return self.sal*self.months
    
class Manager(Employee):
    def __init__(self,name,salary,team_size):
        super().__init__( name,salary)
        self.teamsize=team_size
    def calculate_sal(self):
        return self.sal+(self.teamsize*1000)

reg=RegularEmployee("Rohit",50000,5000)
cont=ContractEmployee("Amit",40000,6)
man=Manager("Deepak",60000,5)
print(reg.calculate_sal())
print(cont.calculate_sal())  
print(man.calculate_sal())

#Vehicle Rental
class Vehicle:
    def __init__(self,model,rentalrate):
        self.model=model
        self.rate=rentalrate
    def Calculate_rental(self,days):
        return self.rate*days
class Car(Vehicle):
    def __init__(self,model,rentalrate,seats)
        super().__init__(model,rentalrate)
        self.seats=seats
    def Calculate_rental(self,days):
        return self.rate*days   
    
class Bike(Vehicle):
    def __init__(self,model,rentalrate,helmetcharge)
        super().__init__(model,rentalrate)
        self.helmet=helmetcharge
    def Calculate_rental(self,days):
        return (self.rate*days)+self.helmet   
class Truck(Vehicle):
    def __init__(self,model,rentalrate,loadcapacity)
            super().__init__(model,rentalrate)
            self.load=loadcapacity
    def Calculate_rental(self,days):
            return (self.rate+self.load*10) * days
car=Car("Honda",1000,5)
bike=Bike("Bullet",500,100)
truck=Truck("Tata",1500,5)
print(car.Calculate_rental(3))
print(bike.Calculate_rental(3))
print(truck.Calculate_rental(3))


            