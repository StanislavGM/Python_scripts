# Function with addition of provided arguments and print user variable value.
def add_numbers(a = 4, b = 0):
    result = a + b
    print("The result is: {}".format(result))
#add_numbers()
#add_numbers(1,3)

def working_on_some(user="root"):
    print("Working with {}".format(user))
    return None
working_on_some("weblogic_admin")