class Dog:
    """Class to create a dog object"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting...")
        print(f"{self.name} is sit.")
    
    def roll(self):
        print(f"{self.name} is rolling...")
        print(f"{self.name} finish rolling.")
    
    def Get_Age(self):
        print(f"{self.name} is {self.age} years old.")

my_dog = Dog('sussie', 10)

my_dog.roll()