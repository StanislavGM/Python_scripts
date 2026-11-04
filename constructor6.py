# Constructor with some functions to print values of the provided arguments.
class emp:
    count = 0
    def get_name_age_salary(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        #self.increase_counf_for_emp()
        #self.display_details()
        return None
    def increase_count_for_emp(self):
        emp.count = emp.count + 1
        return None
    def display_details(self):
        print(f'The name is: {self.name} \n The age is: {self.age} \n The salary is {self.salary}')
        return None
emp1 = emp()
emp2 = emp()
emp1.get_name_age_salary('Johm', 34, 45000)
print(emp1.name)
emp1.increase_count_for_emp()
emp2.get_name_age_salary('Clinton', 25, 54000)
print(emp2.salary)
emp2.increase_count_for_emp()
print(emp.count)