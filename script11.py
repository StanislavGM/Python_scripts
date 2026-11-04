import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.WarningPolicy())

#servers#
stage = ['192.168.221.171']
pre_production = ['192.168.222.123', '192.168.222.98', '192.168.222.99']
production = ['192.168.189.17', '192.168.189.18', '192.168.191.17', '192.168.189.74', '192.168.189.75']

#path
users_xml = '/home/smargalik/clickhouse-server/users.xml'
config_xml = '/home/smargalik/clickhouse-server/config.xml'
path = '/etc/clickhouse-server'

#commands & packages
packages = ' '.join(['clickhouse-server', 'clickhouse-client', 'clickhouse-common-static'])#; pkg_l = ' '.join(packages) #remove_command = 'sudo yum remove -y {}'.format(pkg_l) #install_command = 'sudo yum install -y {}'.format(pkg_l) #print (remove_command,"\n" + install_command)
click_location = '/etc/clickhouse-server'

bkp_configs = 'sudo cp -r /etc/clickhouse-server/ .'
copy_configs = 'sudo cp clickhouse-server/config.xml {0} && sudo cp clickhouse-server/users.xml {0}'.format(click_location)
stop_command = 'sudo systemctl stop clickhouse-server'
start_command = 'sudo systemctl start clickhouse-server'
remove_command = 'sudo yum remove -y {}'.format(packages)
install_command = 'sudo yum install -y {}'.format(packages)

def setup_click (server):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=server, username= 'smargalik', key_filename='C:\\Users\\Test\\.ssh\\id_rsa', port= 22)
        stdin, stdout, stderr = ssh.exec_command('[ -d /home/smargalik/ ] && echo "exist"')
        response = stdout.readlines()[0]
        
        if response == "exist\n":
            cmd_list = [bkp_configs, stop_command,
                        remove_command, install_command, copy_configs]
            for cmd in cmd_list:
                stdin, stdout, stderr = ssh.exec_command(cmd)
                print("The output is: {}".format(stdout.readlines()))
                print("The error is: {}".format(stderr.readlines()))
        
        #print(response)
        
        else:
            cmd_list = [install_command]
            for cmd in cmd_list:
                stdin, stdout, stderr = ssh.exec_command(cmd)
                print("The output is: {}".format(stdout.readlines()))
                print("The error is: {}".format(stderr.readlines()))
        
        ssh.close()
        return None
    except Exception as error:
        print(error)

def trigger():
    for server in stage:
        setup_click(server)
if __name__=="__main__":
    trigger()