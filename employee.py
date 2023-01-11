# The employee class will has several functions and variables

class Employee:
    num_emp = 0
    raise_amt = 1.04



    def __init__(self,first,last,pay):
        self.first = first
        self.last= last
        self.pay = pay
        

    @property
    def email (self):
        return '{}.{}@gmail.com' .format(self.first,self.last)

    @property
    def fullname (self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print ("Employee Deleted")
        self.first = None
        self.last = None

    def apply_raise (self):
        self.pay = (self.pay*self.raise_amt)

    @classmethod
    def set_emp_raise(cls,amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday (day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
    def __repr__(self):

        return "Employee('{}','{}','{}')".format(self.first,self.last, self.pay)
    

#Create a subclass that inheretes attributes from the employee class
class Developer (Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_language):
        super().__init__(first, last, pay)
        self.prog_language = prog_language

# Creating a manager subclass that inherites from the employee class

class Manager (Employee):
    def __init__(self, first, last, pay, employees =None):
        super().__init__(first, last, pay)

        if employees == None:
            self.employees = []

        else:
            self.employees = employees

    def add_employee (self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee (self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname)

        


emp = Employee('joseph','mutua',120000)
emp_1 = Developer('joe','Jane',120000, 'Jave')
emp.last = "James"

print(emp.email)
emp.set_emp_raise(1.05)
print(emp.pay)
emp.apply_raise()
print(emp.pay)

mrg1 = Manager('Joh', 'Joe', 1220000, [emp])

print(mrg1.email)

mrg1.print_employees()
mrg1.add_employee(emp_1)

mrg1.print_employees()
print (emp_1)

emp.fullname = "Jose John"

print (emp.first)
print (emp.last)

    