# Function with addition and substraction.
def addition(a,b):
    print("The addition of {} and {} is: {}".format(a,b,a+b))
    return None
def sub(a,b):
    print("The substraction of {} and {} is {}".format(a,b,a-b))
def main():
    x = 7
    y = 4
    addition(x,y)
    sub(x,y)
    return None
if __name__ == "__main__":
    main()
print("This is from functions1: ", __name__)