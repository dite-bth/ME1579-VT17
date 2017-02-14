from database import db
from models.employee import employee_factory, basic_employee


empf = employee_factory.EmployeeFactory()

print("ALL EMPLOYEES")
# fetch objects /w the most data
result = empf.fetch_all_employees()

for e in result:
    print(e)
    print("-"*(len(e.extension) + len(e.email) + 20))

#########################################
print("\nBASIC EMPLOYEES")
##########################################

result2 = empf.fetch_basic_employees()

for e in result2:
    print(e)

#########################################
print("\nONE EMPLOYEE")
##########################################

andy = empf.fetch_one(1611)
print(andy)

#########################################
print("\nSEARCH")
##########################################

search = empf.search_last_name("b")
for e in search:
    print(e)

#########################################
print("\nOFFICE EMPLOYEES")
##########################################

emps_office = empf.fetch_office_employees(6)
for e in emps_office:
    print(e)


del_emp = empf.fetch_one(1611)
#empf.delete_employee_object(del_emp)