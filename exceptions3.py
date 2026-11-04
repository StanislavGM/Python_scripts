# Handling of known exceptions.
try:
    print("This will be print in first")
    #print(a)
    open("csv_dot.csv")
    #import fabric
except FileNotFoundError:
    print("The file isn't present")
except NameError:
    print("The variable isn't defined")
except TypeError:
    print("Adding number and string isn't possible")
except ZeroDivisionError:
    print("Division by zero isn't possible")
except ModuleNotFoundError:
    print("Please install the module to use it")
except Exception as var:
    print(var)
finally:
    print("Finally this will also be execute")