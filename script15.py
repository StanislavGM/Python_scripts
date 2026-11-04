# Script to print an absolute path of each file with total amount of founded files in the provided path.
import os
path = "C:\\HashiCorp\\Workstation\\Terraform\\Python"
print("------------")
for r, d, f in os.walk(path):
    if len(f) != 0:
        for each_file in f:
            print(os.path.join(r, each_file))
    print(len(f))