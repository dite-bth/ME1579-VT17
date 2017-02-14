from models.employee import basic_employee


class ExtEmployee(basic_employee.BasicEmployee):
    """
        Expandable employee object.
        Populate it /w basic data (arguments to constructor) and use add-methods to
        add data.
        Inherits BasicEmployee.
    """

    def __init__(self, employee_number, first_name, last_name):
        super().__init__(employee_number, first_name, last_name)

        self.extension = None
        self.email = None
        self.job_title = None
        self.reports_to = None
        self.office_code = None

    def add_extension(self, ex):
        """
        Add extension data (argument) to employee object.
        """
        self.extension = ex


    def add_email(self, email):
        """
        Add email data (argument) to employee object.
        """
        self.email = email


    def add_office_code(self, office):
        """
        Add office code data (argument) to employee object.
        """
        self.office_code = office


    def add_reports_to(self, boss):
        """
        Add reports to data (argument) to employee object.
        """
        self.reports_to = boss


    def add_job_title(self, job):
        """
        Add job title data (argument) to employee object.
        """
        self.job_title = job


    def __str__(self):
        tmp = self.first_name+ " " + self.last_name
        tmp = tmp + " - " + str(self.job_title)
        tmp = tmp + "\nExtension: " + str(self.extension) + ", Email: " + str(self.email)
        tmp = tmp + "\nReports to: " + str(self.reports_to) + "\nOffice code: " + \
                    str(self.office_code)

        return tmp
