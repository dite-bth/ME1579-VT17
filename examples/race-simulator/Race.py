from Car import CombustionEngineCar, ElectricEngineCar
import random


class Race():
    """ Representing characteristics of a car race """
    def __init__(self, name, length, competing_cars):
        self.name = name
        # Length of race in km
        self.length = length
        # List of cars
        self.competing_cars = competing_cars
        # Empty dictionary for storing race result
        self.results = {}

    def run(self):
        """ Run race and store each car in an ordered list with race time as key """
        for car in self.competing_cars:
            if isinstance(car, CombustionEngineCar):
                # Race calculation for combustion engine car

                # Calculate estimated drive time (in a simplified way not att all correct IRL)
                estimated_time = self.length / (1000 * car.power / car.weight) * 60 * 60

                # Adding luck factor to get drive time
                drive_time = int(estimated_time * random.uniform(0.8, 1.2))

                # Number of filled fuel tanks to finish race
                refills = int(self.length / (car.fuel_tank_size / car.fuel_economy * 100))

                # Time in depot
                depot_time = int(refills * car.refuel_time)

                race_time = drive_time + depot_time

                # Add data to result dictionary
                self.results[race_time] = car

            elif isinstance(car, ElectricEngineCar):
                # Race calculation for electric engine car

                # Calculate estimated drive time (in a simplified way not att all correct IRL)
                estimated_time = self.length / (1000 * car.power / car.weight) * 60 * 60

                # Adding luck factor to get drive time
                drive_time = int(estimated_time * random.uniform(0.8, 1.2))

                # Number of battery charges to finish race
                charges = int(self.length / (car.battery_capacity / car.power_consumption * 100))

                # Time in depot
                depot_time = int(charges * car.charging_time)

                race_time = drive_time + depot_time

                # Add data to result dictionary
                self.results[race_time] = car


