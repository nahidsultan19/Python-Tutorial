
class Employee:

    raise_amt = 1.05
    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = f'{firstName}{lastName}@email.com'

    def fullName(self):
        # return f'{self.firstName}{self.lastName}'
        return '{} {}'.format(self.firstName, self.lastName)

    def increment(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    def __init__(self, firstName, lastName, pay, programming_lang=None):
        super(Developer, self).__init__(firstName, lastName, pay)
        self.programming_lang = programming_lang


class Manager(Employee):
    def __init__(self, firstName, lastName, pay, employees=None):
        super(Manager, self).__init__(firstName, lastName, pay)
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

    def show_emp(self):
        for emp in self.employees:
            print('------>',emp.fullName().capitalize())


Emp_1 = Employee('nahid','sultan', 90000)
Emp_2 = Employee('mamun', 'rashid', 90000)

Dev_1 = Developer('nahid', 'sultan', 90000, 'Python')
Dev_2 = Developer('mamun', 'rashid', 90000, 'Java')

Mgr = Manager('ariful', 'islam', 100000, [Dev_1])

# Employee Details
print("-------------------Employee Details--------------")
print('-------------------------------------------------')
print(f'Employee_1 Fullname is:', Emp_1.fullName().capitalize())
print(f'Employee_1 Email is:', Emp_1.email)
print(f'Employee_1 current salary is:', Emp_1.pay)
Emp_1.increment()
print(f'Increment Salary is:', Emp_1.pay)
print('-------------------------------------------------')

# Developer Details
print('-----------------Developer Details---------------')
print('-------------------------------------------------')

print(f'Developer Fullname is:', Dev_1.fullName().capitalize())
print(f'Developer Email is:', Dev_1.email)
print(f'Developer current salary is:', Dev_1.pay)
Dev_1.increment()
print(f'Developer increment salary is:', Dev_1.pay)
print(f'Developer Programming language is:', Dev_1.programming_lang)

# Manager Section
print('---------------Manager Details-------------------')
print('-------------------------------------------------')

print(f'Manager FullName is:', Mgr.fullName().capitalize())
print(f'Manager Email is:', Mgr.email)
print(f'Manager current salary is:', Mgr.pay)
Mgr.increment()
print(f'Manager increment salary is:', Mgr.pay)
print('-------------------------------------------------')

print('-------  Developer under of Manager -------------')
Mgr.add_emp(Dev_2)
# Mgr.remove_emp(Dev_1)
Mgr.show_emp()