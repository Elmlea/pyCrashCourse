class Car:
    # A simple attempt to represent a car

    def __init__(self, make, model, year):
        # Initialise the attributes to define the car
        self.make = make # the attribute self.make is taken from the parameter make passed when the instance is created
        self.model = model
        self.year = year
        self.odometer_reading = 0
        # If you want a default value for an attribute, pass it like this; don't add it in the "init" statement.
        # Only those that need parameters passed when the instance is created

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        # Prints a statement with the defined current mileage
        print(f"This car has covered {self.odometer_reading} miles.")

    def update_odometer(self, mileage):
        # This will set the odometer attribute to the given value
        self.odometer_reading = mileage

my_new_car = Car('lotus', 'elise', 2001)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()
my_new_car.odometer_reading = 2500
my_new_car.read_odometer()
my_new_car.update_odometer(10000)
my_new_car.read_odometer()