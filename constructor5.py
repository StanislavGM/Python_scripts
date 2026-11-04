# Constructor with function to sum of the two objects.
class calculator:
    number1 = 6
    number2 = 8
    def sum(self, a, b):
        sum = a + b
        return sum
obj = calculator()
print(obj.number1)
sumvalue = obj.sum(6, 10)
print(sumvalue)