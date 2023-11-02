import datetime

from employee import Employee
from tester import Tester
from developer import Developer
from dataclasses import dataclass


# Saves to write __init__ etc. for simple storage types.
# For dataclasses slots can be implemented using the decorator.
@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str


def main() -> int:
    employee1 = Employee("Max Mustermann", 30, 3870)
    employee1.increase_salary(25)
    print(employee1)
    print(repr(employee1))
    employee2 = eval(repr(employee1))
    print(employee2.salary)
    # employee2.salary = 990 Would raise now ValueError

    employee3 = Tester("Lauren", 44, 1000)
    employee4 = Developer("Ji-Soo", 38, 1000, "Flask")
    print(employee4.__slots__)
    print(employee4.has_slots())
    print(employee1.minimum_wage)
    print(isinstance(employee3, Tester))
    print(isinstance(employee3, Employee))

    print(issubclass(Developer, Employee))
    print(issubclass(Employee, object))
    print(issubclass(Developer, object))

    employee5 = Employee.new_employee("Hermine Musterfrau", datetime.date(1990, 11, 2))
    print(employee5)

    project = Project("Some Project", 20000, "Some Client")
    return 0


main()
