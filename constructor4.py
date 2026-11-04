# Constructor init method.
'''
class Emp:
    def display(self):
        print("This is a display method")
        return None
emp1 = Emp()
emp2 = Emp()
emp1.display()
emp2.display()
'''
class Emp(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.display()
        return None
    def display(self):
        print(f'The name is: {self.name} \n The salary is: {self.salary}')

emp1 = Emp('Ramu', 45000)
emp2 = Emp('Naren', 56000)
#emp1.display()
#emp2.display()