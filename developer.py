from employee import Employee
from slotsInspectorMixin import SlotsInspectorMixin


class Developer(SlotsInspectorMixin, Employee):  # When doing method resolution, the order Parent classes are defined
    # matter.

    # Offers faster access of attributes + reduces memory overhead
    # Tradeoff: New attributes can not be added dynamically later:
    # e.g.: developer1.new_attribute = 2
    __slots__ = ("framework",)

    def __init__(self, name, age, salary, framework) -> None:
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0) -> None:
        super().increase_salary(percent)
        self.salary += bonus

    # def has_slots(self) -> bool:
    # return hasattr(self, "__slots__")
