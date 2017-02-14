"""
Database connection handler.
"""

import mysql.connector
from database import db_config

class Db():
    """
        Handles database connection to mysql (depense on mysql-connector package,
        see: https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html).
        Exposes a few methods to connect to, execute a query and close a mysql database connection.
    """

    def __init__(self):
        self.con = mysql.connector.connect(**db_config.config)
        self.cursor = self.con.cursor()


    def query(self, query):
        """
        Executes a query (argument) to mysql database and returns the cursor /w
        a fetchall() call.
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()


    def close(self):
        """
        Closes the mysql connection.
        """
        self.cursor.close()
        self.con.close()
