# Functions with exception handlers to print the changed working directory.
import os
def main():
    req_path = input("Enter a path to change working directory: ")
    print("The current working directory is: ", os.getcwd())
    try:
        os.chdir(req_path)
        print("Now your new working dir is: ", os.getcwd())
    except FileNotFoundError:
        print("The givern path isn't a valid path. So can't change the working directory")
    except NotADirectoryError:
        print("The given path is a file path. So can't change the working directory")
    except PermissionError:
        print("Sorry you don't have access for the given path. So can't change the working directory")
    except Exception:
        print(Exception)
if __name__=="__main__":
    main()