# Script to execute the command on the remote server and print result.
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())
ssh.connect(hostname = '', username = '', password = '', port = 22)
stdin, stdout, stderr = ssh.exec_command('dir')
print("The output is: ")
print(stdout.readline())
print("The error is: ")
print(stderr.readlines())