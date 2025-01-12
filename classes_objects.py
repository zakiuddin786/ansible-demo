# Defining the class
class Car:
    def __init__(self, brand, model, year, energy_type, colour, avg_mileage, state , on_road_price, owner):
        self.brand = brand
        self.model = model
        self.year = year
        self.energy_type = energy_type
        self.colour = colour
        self.avg_mileage = avg_mileage
        self.state = state
        self.on_road_price = on_road_price
        self.owner = owner


    def start_engine(self):
        if(self.energy_type == "Electric"):
            print(f"{self.owner}'s car {self.brand} 's with model {self.model} is of type {self.energy_type} and will start using battery")
        else:
            print(f" {self.owner}'s car {self.brand} with model {self.model} engine is started")

# Created an instance of the class ( Object is created)
nayan_car = Car("BMW", "Z4", "2025", "Petrol", "Red", 8, "MH", "2.24 cr", "Nayan")

# Accessing the attributes of the class
print(f"{nayan_car.owner} got a {nayan_car.brand} car with model {nayan_car.model} of {nayan_car.colour} Colour which gives an average mileage of {nayan_car.avg_mileage}")

nayan_car.start_engine()

ashutosh_car = Car("Toyota", "Supra", "2025", "Electric", "Black", 8, "MH", "85 Lakhs", "Ashutosh")
print(f"{ashutosh_car.owner} got a {ashutosh_car.brand} car with model {ashutosh_car.model} of {ashutosh_car.colour} Colour which gives an average mileage of {ashutosh_car.avg_mileage}")

ashutosh_car.start_engine()


