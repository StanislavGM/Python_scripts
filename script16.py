# Script to make ssh connection and copy/download the provided file to/from the target server.
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='', username= 'smargalik', key_filename='C:\\Users\\Test\\.ssh\\id_rsa', port= 22) #password= ''
sftp_client = ssh.open_sftp()
#sftp_client.chdir('/home/smargalik')
#print(sftp_client.getcwd())# - проверка доступных функций
#sftp_client.get('rules.yml', 'C:\\Terraform\\Workstation\\Terraform\\Python\\rules.yml')
sftp_client.put('C:\\Users\\Test\\Downloads\\nexus3-3.70.1.02-1.el9.x86_64.rpm', '/home/smargalik/nexus3-3.70.1.02-1.el9.x86_64.rpm')
'''
sftp_client.chdir('/home/palmn_dev/test/ssh')
sftp_client/.get('downloaded_file.txt', 'C:\\Users\Administrator\\Downloads\\downloaded_file.txt') # -- загрузка файла с уд. сервера
print(sftp_client.getcwd()) - проверка доступных функций
sftp_client.close()
ssh.close()
'''
#sftp_client.put('Python.rar', '/home/palmn_dev/test/ssh/Python.rar')
sftp_client.close()
ssh.close()