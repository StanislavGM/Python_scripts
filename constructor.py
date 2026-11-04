# Constructor and destructor.

class Person(object):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        print("An object has been created {} {}".format(self.name, self.age))
        return  None
    def __del__(self):
        print("An object has been deleted")
        return None
per1 = Person('John', 26)