from employee import Employee


class Tester(Employee):
    def run_tests(self) -> None:
        print(f'Testing is started by {self.name}...')
        print('Tests are done.')

