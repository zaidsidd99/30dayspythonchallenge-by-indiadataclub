from electric_car import ElectricCar

car_1 = ElectricCar("tata", "nexon", 2024, "white", 60)

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.colour)

car_1.drive()
car_1.stop()
car_1.describe_battery()
car_1.charge()