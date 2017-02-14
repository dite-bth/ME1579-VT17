"""
Expands BasicEmployee /w all data related to employee object.
Inherits BasicEmployee
"""

from models.employee import basic_employee

class Employee(basic_employee.BasicEmployee):
    """
    Expands BasicEmployee /w all data related to employee object.
    Inherits BasicEmployee
    """

    def __init__(self, employee_number, first_name, last_name, extension,
                 email, office_code, reports_to, job_title):
        super().__init__(employee_number, first_name, last_name)
        self.extension = str(extension)
        self.email = str(email)
        self.office_code = office_code
        self.reports_to = reports_to
        self.job_title = job_title


    def __str__(self):
        tmp = self.first_name + " " + self.last_name
        tmp = tmp + " - " + str(self.job_title)
        tmp = tmp + "\nExtension: " + str(self.extension) + ", Email: " + str(self.email)
        tmp = tmp + "\nReports to: " + str(self.reports_to) + \
                    "\nOffice code: " + str(self.office_code)
        return tmp
