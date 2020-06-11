class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age
        # This is taking the PARAMETER name passed when the instance is created, and assigning it to the VARIABLE name.
        # The VARIABLE is attached to the instance.  They're called ATTRIBUTES.
        # The SELF prefix makes this variable accessible to any method in the class.

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    # These methods are defined with only SELF as a parameter.  Each instance will have access.

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"He is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name}.")
print(f"She is {your_dog.age} years old.")

your_dog.sit()