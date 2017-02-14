"""
Employee factory class.

Creates objects, populated from database table employee.
"""

from database import db
from models.employee import employee, basic_employee, ext_employee

class EmployeeFactory():
    """
    Employee factory class.
    Exposes three methods to populate employee objects with different amounts of data in them.
    """


    def __init__(self):
        self._mysql = None


    def _connect(self):
        self._mysql = db.Db()


    def _close(self):
        self._mysql.close()


    def fetch_basic_employees(self, limit=100):
        """
        Returns a list with BasicEmployee objects.
        Objects populated with employeeNumber, firstName and lastName
        """

        self._connect()

        query = "SELECT employeeNumber, firstName, lastName FROM employees"
        if limit > 100:
            query = "SELECT employeeNumber, firstName, lastName FROM employees LIMIT " + str(limit)

        rows = self._mysql.query(query)

        employees = []

        for row in rows:
            tmp = basic_employee.BasicEmployee(row[0], row[1], row[2])
            employees.append(tmp)

        self._close()

        return employees


    def fetch_all_employees(self):
        """
        Returns a list with Employee objects.
        Objects populated with all table data; employeeNumber, firstName and lastName,
        extension, email, officeCode, reportsTo and jobTitle.
        """

        self._connect()


        query = "SELECT employeeNumber, firstName, lastName, extension, email,\
                 officeCode, reportsTo, jobTitle FROM employees"

        rows = self._mysql.query(query)

        employees = []

        for row in rows:
            # splits the tuple (row) into variables;
            # each element is extracted into corresponding variable
            emp_nbr, first_name, l_name, extension, email, office_c, reports_to, job = row

            tmp = employee.Employee(emp_nbr, first_name, l_name,\
                                    extension, email, office_c, reports_to, job)
            employees.append(tmp)

        self._close()
        return employees


    def fetch_ext_employees(self):
        """
        Returns a list with ExtEmployee (extendable) objects.
        Objects populated with employeeNumber, firstName and lastName.
        """

        self._connect()

        query = "SELECT employeeNumber, firstName, lastName, email, jobTitle FROM employees"

        rows = self._mysql.query(query)

        employees = []
        for row in rows:
            tmp = ext_employee.ExtEmployee(row[0], row[1], row[2])
            tmp.add_email(row[3])
            tmp.add_job_title(row[4])

            employees.append(tmp)

        self._close()

        return employees

    def fetch_one(self, employee_number):
        """
        Fetch one employee by the employee number (argument).
        Returns a BasicEmployee object.
        """
        self._connect()

        query = "SELECT employeeNumber, firstName, lastName FROM employees\
                 WHERE employeeNumber=" + str(employee_number)

        rows = self._mysql.query(query)

        emp = None
        for row in rows:
            emp = basic_employee.BasicEmployee(row[0], row[1], row[2])

        self._close()

        return emp

    def search_last_name(self, last_name_starts_with):
        """
        Search the database for an employee, by last name.
        Returns a list /w found entries, populated /w BasicEmployee-objects,
        where last name starts /w argument string.
        """

        self._connect()

        query = "SELECT employeeNumber, firstName, lastName FROM employees\
                 WHERE lastName LIKE '" + last_name_starts_with + "%'"

        rows = self._mysql.query(query)

        employees = []

        for row in rows:
            en, fn, ln = row
            tmp = basic_employee.BasicEmployee(en, fn, ln)
            employees.append(tmp)

        self._close()

        return employees

    def fetch_office_employees(self, office_code):
        """
        Returns a list /w all employees (BasicEmployees)
        working at a specific office (argument).
        """
        self._connect()

        query = "SELECT employeeNumber, firstName, lastName FROM employees\
                 WHERE officeCode = " + str(office_code)

        rows = self._mysql.query(query)

        employees = []

        for row in rows:
            tmp = basic_employee.BasicEmployee(row[0], row[1], row[2])
            employees.append(tmp)

        self._close()

        return employees

    def delete_employee_object(self, employee_obj):
        """
        Deletes supplied employee object (any of type BasicEmployee object) from database.
        """
        self._connect()

        query = "DELETE FROM employees WHERE employeeNumber=" + str(employee_obj.employee_number)
        self._mysql.query(query)

        self._close()


    def create_employee(self, new_employee):
        """
        Creates a new employee row in database, given the object (argument).
        Object must be of type Employee.
        """
        # TO-DO
