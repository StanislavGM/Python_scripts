# Script to create csv file.
import csv
req_file = "C:\\Terraform\\Workstation\\Terraform\\Python\\csv_file.csv"
fo = open(req_file, 'r')
content = csv.reader(fo, delimiter='|')
#print(f'The header is: \n {list(content)[0]}') Способ №-1
header = next(content)
#print('The header is: ', header) Способ №-2
print('The number of rows are: ', len(list(content))-1)
fo.close()