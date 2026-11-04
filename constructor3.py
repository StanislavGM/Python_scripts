# Constructor encapsulation.
class Person(object):
    def assign_name_and_age(self, name, age):
        self.name = name
        self.__age = age
        self.__display()
        return None
    def __display(self):
        print(self.name, self.__age)
        return None
per1 = Person()
#print(per1.__age) -- команда выполнена не будет, т.к. инкапсуляция была включена для данной переменной
# per1.__display() -- команда выполнена не будет, т.к. инкапсуляция была включена для данного метода
per1.assign_name_and_age('Naren', 20) # несмотря на включенную инкапсуляцию метода __display() и переменной __age, они по прежнему доступны внутри класса.