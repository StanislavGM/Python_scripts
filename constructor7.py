# Constructor with functions to print file directory name
import os

class Terraform:
    def get_details_for_each_tomcat(self,server_xml):
        self.tf = server_xml
        self.th = os.path.dirname(os.path.dirname(server_xml))
        return None
    def display_details(self):
        print('The terraform config file is: {}\n The terraform path is: {}'.format(self.tf,self.th))
        return None
def general():
    terraform_primary = Terraform()
    terraform_secondary = Terraform()
    terraform_primary.get_details_for_each_tomcat('C:\\Terraform\\Workstation\\Terraform\\terraform.tf')
    terraform_secondary.get_details_for_each_tomcat('C:\\Users\\Administrator\\Documents\\Workstation\\Terraform\\terraform.tf')
    terraform_primary.display_details()
    terraform_secondary.display_details()
if __name__ == "__main__":
    general()