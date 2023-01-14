import paramiko
import subprocess
import pytest
from subprocess import Popen, PIPE

@pytest.fixture(scope="function")
def server():
    server_ip = "192.168.0.100"
    password = "hj,jn1337"
    username = "denis"
    command = 'iperf -s'
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(hostname=server_ip, port=port, username=username, password=password)
    stderr = ssh.exec_command(command)
    yield stderr
    ssh.close()

@pytest.fixture(scope='function')
def client():
    server_ip = "192.168.0.100"
    process = Popen(['iperf', '-c', server_ip, '-i 1'], stdout=PIPE, stderr=PIPE)
    return process.communicate()
