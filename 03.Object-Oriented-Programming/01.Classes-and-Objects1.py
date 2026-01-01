class Bike:
    # Defining the attributes of a Class
    color = None
    tyre_size = None
    price = None
    fuel_type = None

    # Defining the behavior of the Class
    def RideType(self):
        print("Move Forward")

    # Displaying the attributes of the Bike
    def displayBikeDetails(self):
        print("Bike Color:", self.color)
        print("Bike Tyre Size:", self.tyre_size)
        print("Bike Price:", self.price)
        print("Bike Fuel Type:", self.fuel_type)

# Creating an Object of the Class Bike
bike1 = Bike()
bike1.color = "Blue"
bike1.tyre_size = 16
bike1.price = 10000
bike1.fuel_type = "Petrol"
bike1.displayBikeDetails()

# Creating another Object of the Class Bike 
bike2 = Bike()
bike2.color = "Red"
bike2.tyre_size = 20
bike2.price = 23000
bike2.fuel_type = "Diesel"
bike2.displayBikeDetails()

# If we don't assign any value to the attributes, they will have the default value None