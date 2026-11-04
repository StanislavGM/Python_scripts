import csv
req_file = "C:\\Terraform\\Workstation\\Terraform\\Python\\csv_file.csv"
my_data = [['S_No', 'Name', 'Age'], [1, 'Json', 23], [2, 'Jonathan', 21], [3, 'Jake', 33]]
fo = open(req_file, 'w', newline="")
csv_writer = csv.writer(fo, delimiter="|")
csv_writer.writerows(my_data)
#csv_writer.writerow(["S_No", "Name", "Age"])
#csv_writer.writerow([1, "Json", 23])
fo.close