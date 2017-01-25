
class Car():
    """ Representing characteristics of a car """

    def __init__(self, brand, model, year, power, weight):
        """ Initiate object. """
        self.brand = brand
        self.model = model
        self.year = year
        # Engine power in kW, affects: acceleration
        self.power = power
        # Weight in kg, affects: acceleration, braking distance, traction, fuel consumption, tyre wear
        self.weight = weight


class CombustionEngineCar(Car):
    """ Representing characteristics of a car with an internal combustion engine """

    def __init__(self, brand, model, year, power, weight, fuel_tank_size, fuel_economy):
        """ Initiate object. """

        # Size of fuel tank in liters, affects: distance
        self.fuel_tank_size = fuel_tank_size
        # Fuel economy as liters per 100 kilometers, affects: distance
        self.fuel_economy = fuel_economy
        # Time to fill tank in seconds (tank size * 3s)
        self.refuel_time = fuel_tank_size * 3

        # Initialize attributes of the parent class
        super().__init__(brand, model, year, power, weight)


class ElectricEngineCar(Car):
    """ Representing characteristics of a car with an electrical engine """

    def __init__(self, brand, model, year, power, weight, battery_capacity, power_consumption, charging_time):
        """ Initiate object. """

        # Power capacity of battery in kWh, affects: distance
        self.battery_capacity = battery_capacity
        # Power consumption as kWh per 100 miles, affects: distance
        self.power_consumption = power_consumption
        # Time to charge battery in seconds
        self.charging_time = charging_time

        # Initialize attributes of the parent class.
        super().__init__(brand, model, year, power, weight)


