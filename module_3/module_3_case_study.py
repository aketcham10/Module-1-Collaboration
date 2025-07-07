class Vehicle:
    def __init__(self, type):
        self.type = type


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("Car")
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


def main():
    type = input("Enter vehicle type: ")
    if type.capitalize() == "Car":
        vehicle = Vehicle(type)
        year = input("Enter year: ")
        make = input("Enter make: ")
        model = input("Enter model: ")
        doors = input("Enter number of doors: ")
        roof = input("Enter roof type: ")
        automobile = Automobile(year, make, model, doors, roof)
        print(f"Year: {automobile.year}")
        print(f"Make: {automobile.make}")
        print(f"Model: {automobile.model}")
        print(f"Number of doors: {automobile.doors}")
        print(f"Roof type: {automobile.roof}")
    else:
        print("Invalid vehicle type.")


if __name__ == "__main__":
    main()