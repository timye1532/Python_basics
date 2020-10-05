import sys
import datetime

class Employee():

    '''class variables '''
    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first_name, last_name, salary):
        '''
            init function
        '''
        self.first_name = first_name
        self.last_name = last_name
#        self.email = first_name + "." + last_name + "@some.com"
        self.salary = int(salary)
        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first_name, self.last_name)

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first_name = None
        self.last_name = None

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        '''
            Use classmethod as alternative constructors
        '''
        first_name, last_name, salary = emp_str.split('-')
        p = cls(first_name, last_name, salary)
        return p

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.salary)

    def __str__(self):
        return '{} -- {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.salary + other.salary
    
    def __len__(self):
        return len(self.fullname())

class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first_name, last_name, salary, prog_lang):
        super(Developer, self).__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first_name, last_name, salary, employees=None):
        super(Manager, self).__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


if __name__ == "__main__":

    emp1 = Employee('Jason', 'Smith', 100)
    emp2 = Employee('Tom', 'schafer', 120)

    dev_1 = Developer('Corey', 'Schafer', 500, 'Python')
    mgr_1 = Manager('Sue', 'Smith', 900, [dev_1])

    emp_str_1 = 'John-Doe-200'
    emp_str_2 = 'Steve-Smith-150'

    emp1_s = Employee.from_string(emp_str_1)
    emp2_s = Employee.from_string(emp_str_2)
    
