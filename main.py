from employee import Employee


def main() -> int:
    employee1 = Employee("Max Mustermann", 30, "Software Developer", 3870)
    employee1.increase_salary(25)
    print(employee1)
    print(repr(employee1))
    employee2 = eval(repr(employee1))
    print(employee2.salary)
    # employee2.salary = 990 Would raise now ValueError
    return 0

main()