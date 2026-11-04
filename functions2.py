# Function with import a file with function included addition and substraction.
import Python.functions1 as functions1

def mult(a,b):
    print("The mul of {} and {} is: {}".format(a,b,a*b))
    return None
def main():
    x = 20
    y = 10
    functions1.addition(x,y)
    functions1.sub(x,y)
    mult(x,y)
    return None
if __name__ == "__main__":
    main()
print("This is from functions2: ", __name__)