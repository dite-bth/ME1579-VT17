from flask import Flask
from Car import CombustionEngineCar, ElectricEngineCar
from Race import Race
import json

app = Flask(__name__)


def complexhandler(obj):
    """ Function for enabling nested objects to be converted to JSON """
    return obj.__dict__


@app.route('/race')
def show_race():
    car0 = CombustionEngineCar("Lotus", "Elise SC", 2007, 162, 903, 43.5, 8.5)
    car1 = CombustionEngineCar("Subaru", "WRX STI", 2017, 227, 1538, 60, 10.5)

    # Create a race
    race = Race("Monaco", 1200, [car0, car1])

    # Run race
    race.run()

    # Return result
    return json.dumps(race, default=complexhandler)


if __name__ == '__main__':
    app.run(debug=True)
