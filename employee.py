# In Python the constructor is split into two different functions.
# OOP Languages like C#, C++, Java have simply a constructor, not so
# in Python. The creation and the initialization is split:
# __new__
# __init__
# Methods with two underscores are called Dunder Methods. Never name own methods with double underscore!

class Employee:
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent) -> None:
        self.salary += self.salary * (percent / 100)

    # like toString overload in Java.
    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}'

    # returns also a string, but should be used to make this instance reproducible.
    # --> Should return the construction call of the object. Used for developers.
    def __repr__(self) -> str:
        return (
                f'Employee('
                f'{repr(self.name)}, {repr(self.age)}, '
                f'{repr(self.position)}, {repr(self.salary)})'
                )

    @property
    def salary(self) -> int:
        return self._salary

    # The decorator needs the name of the property, in this case salary defined in line 32.
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary

    @property
    def annual_salary(self) -> int:
        return self.salary * 12

