# Functions to print file directory name
import os

# Method 1 -- when get_details and display get called in order for each terraform file.
'''
def get_details_for_each_terraform(server_xml):
    global tf, th
    tf = server_xml
    th = os.path.dirname(os.path.dirname(server_xml))
    return None
def display_details():
    print('The Terraform config file is: {} \n The Terraform path is: {}'.format(tf,th))
    return None
def general():
    terraform_primary = 'C:\\Terraform\\Workstation\\Terraform\\terraform.tf'
    terraform_secondary = 'C:\\Users\\Administrator\\Documents\\Workstation\\Terraform\\terraform.tf'

    get_details_for_each_terraform(terraform_primary)

    display_details()

    get_details_for_each_terraform(terraform_secondary)

    display_details()

    return None

if __name__=="__main__":
    general()
'''
# Method 2 -- get_details and display are using together. In this example we use different variable names to print out its content.
def get_details_for_each_terraform(server_xml):
    global tf, th
    tf = server_xml
    th = os.path.dirname(os.path.dirname(server_xml))
    return tf, th

def display_details():
    print('The Terraform config file is: {} \n The Terraform path is: {}'.format(tf,th))
    return None

def general():
    terraform_primary = 'C:\\Terraform\\Workstation\\Terraform\\terraform.tf'
    terraform_secondary = 'C:\\Users\\Administrator\\Documents\\Workstation\\Terraform\\terraform.tf'

    # применяем переменные
    terraform_file, terraform_home = get_details_for_each_terraform(terraform_primary)

    get_details_for_each_terraform(terraform_secondary)

    display_details()

    print('The Terraform config file is: {} \n The Terraform path is: {}'.format(terraform_file, terraform_home))

    return None

if __name__=="__main__":
    general()