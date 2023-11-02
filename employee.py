from datetime import date


# In Python the constructor is split into two different functions.
# OOP Languages like C#, C++, Java have simply a constructor, not so
# in Python. The creation and the initialization is split:
# __new__
# __init__
# Methods with two underscores are called Dunder Methods. Never name own methods with double underscore!

class Employee:
    minimum_wage = 1000

    # There is also the @staticmethod keyword to define a static method. But this shouldn't be used. Even the
    # creator of python said, that it was only a placeholder for the static concept of other languages, until
    # they came up with @classmethod. Simply no reason to use @staticmethod.
    @classmethod
    def change_minimum_wage(cls, new_wage) -> None:
        if new_wage > 3000:
            raise ValueError("The minimum_wage should not be higher than $3000")
        else:
            Employee.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    __slots__ = ("name", "age", "_salary")

    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent) -> None:
        self.salary += self.salary * (percent / 100)

    # like toString overload in Java.
    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old. Employee has a salary of ${self.salary}'

    # returns also a string, but should be used to make this instance reproducible.
    # --> Should return the construction call of the object. Used for developers.
    def __repr__(self) -> str:
        return (
                f'Employee('
                f'{repr(self.name)}, {repr(self.age)}, '
                f'{repr(self.salary)})'
                )

    @property
    def salary(self) -> int:
        return self._salary

    # The decorator needs the name of the property, in this case salary defined in line 32.
    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f'Minimum wage is {Employee.minimum_wage}')
        self._salary = salary

    @property
    def annual_salary(self) -> int:
        return self.salary * 12

