class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Car Information:")
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)


class Electric_Car(Car):
    def __init__(self, make, model, year, battery_status):
        super().__init__(make, model, year)
        self.battery_status= battery_status

    def display_info(self):
        super().display_info()
        print("Battery Capacity:", self.battery_status)

    def charge(self):
        print("Charging the electric car...")


# Create an instance of the Car class and display its information
car1 = Car("Toyota", "Camry", 2022)
car1.display_info()

print()

# Create an instance of the ElectricCar class and display its information
electric_car = Electric_Car("Tesla", "Model S", 2023, "100 kWh")
electric_car.display_info()
electric_car.charge()
