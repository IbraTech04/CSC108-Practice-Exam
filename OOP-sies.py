class Vehicle:
    def __init__(self, make, model, year, efficiency):
        self.make = make
        self.model = model
        self.year = year
        self.efficiency = efficiency
        self.gas = 100
    
    def drive(self, distance: int) -> None:
        if self.gas <= 0:
            print("Out of gas!")
            return
        self.gas -= distance / self.efficiency

    def refuel(self) -> None:
        self.gas = 100
        print("Refueled!")
    
    def __str__(self) -> str:
        return f"This is a {self.year} gas-guzzling {self.make} {self.model} with {self.gas}% gas remaining."

class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, efficiency, battery_size):
        super().__init__(make, model, year, efficiency)
        self.battery = battery_size
    
    def drive(self, distance: int) -> None:
        if self.battery <= 0:
            print("Out of battery!")
            return
        self.battery -= distance / self.efficiency  
    
    def recharge(self) -> None:
        self.battery = 100
        print("Recharged!")
    
    def __str__(self) -> str:
        return f"This is a {self.year} electric {self.make} {self.model} with {self.battery}% battery remaining and FSD beta."

# What is the output of the following code?
tesla = ElectricVehicle("Tesla", "Model S", 2023, 0.3, 100)
print(tesla.gas)
Vehicle.drive(tesla, 100)

toyota = Vehicle("Toyota", "Corolla", 2005, 0.1)
ElectricVehicle.drive(toyota, 100)

# Is the following output possible? 

# This is a 2023 electric Tesla Model S with 100% battery remaining and FSD beta.
