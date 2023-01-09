# The employee class will has several functions and variables

class Employee:
    num_emp = 0
    raise_amt = 1.04



    def __init__(self,first,last,pay):
        self.first = first
        self.last= last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname (self):
        return '{} {}'.format(self.first, self.last)
    
    def sal_raise (self):
        self.pay = (self.pay*self.raise_amt)




emp = Employee('joseph','mutua',120000)

print (emp.email)
print (emp.fullname())
print (emp.pay)


    