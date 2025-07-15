# class Human:
#     def __init__(self, name, occupation):
#         self.name = name
#         self.occupation = occupation

#     def do_work(self):
#         if self.occupation == "tennis player":
#             print(self.name, "plays tennis")
#         elif self.occupation == "actor":
#             print(self.name, "shoots films")

#     def speaks(self):
#         print(self.name, "says how are you?")


# tom = Human("tom cruise", "actor")
# tom.do_work()
# tom.speaks()

# maria = Human("maria lous", "tennis player")
# maria.do_work()
# maria.speaks()




# class microwave:
#     def __init__ (self, brand:str,power_rating:str):
#         self.brand =brand
#         self.power_rating=power_rating

# smeg: microwave= microwave(brand='smeg',power_rating='B')

# print(smeg)
# print(smeg.brand)
# print(smeg.power_rating)

# bosch:microwave=microwave(brand='bosch',power_rating='C')
# print(bosch)
# print(bosch.brand)
# print(bosch.power_rating)

# Lg:microwave=microwave(brand='Lg',power_rating='A')
# print(Lg)
# print(Lg.brand)
# print(Lg.power_rating)


# summercool:microwave=microwave(brand='summercool',power_rating='B')
# print(summercool)
# print(summercool.brand)
# print(summercool.power_rating)




#######################################################



# Create a Car class with attributes and a display method ?

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand        # Car brand (e.g. maruti)
        self.model = model        # Car model (e.g. tata)
        self.year = year          # Manufacturing year

    def display(self):
        print("Car Details:")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


# Creating objects of the Car class
car1 = Car("Toyota", "Tata", 2020)
car2 = Car("Honda", "City", 2022)

# Calling the display method
car1.display()
car2.display()
