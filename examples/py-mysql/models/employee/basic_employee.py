"""
Basic Employee /w basic data.
"""


class BasicEmployee():
    """
    Basic Employee /w basic data.
    """

    def __init__(self, employee_number, first_name, last_name):
        self.employee_number = employee_number
        self.first_name = first_name
        self.last_name = last_name


    def __str__(self):
        return str(self.employee_number) + ": " + self.first_name + " " + self.last_name
