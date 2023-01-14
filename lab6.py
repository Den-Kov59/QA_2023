from subprocess import Popen, PIPE

server_ip = '192.168.0.100'

def client(server_ip):
    process = Popen(['iperf', '-c', server_ip, '-i 1'], stdout=PIPE, stderr=PIPE)
    return process.communicate()

def parser(result):
    result = result.split('\n')
    parsed_result = []
    for line in result:
        line = line.split(' ')
        interval =''
        transfer = 0
        bandwith = 0
        for n in range(len(line)):
            if(line[n] == 'sec'):
                interval = line[n-2][2:]+line[n-1]
            elif(line[n] == 'MBytes'):
                transfer = float(line[n-1])
            elif(line[n] == 'Mbits/sec'):
                bandwith = float(line[n-1])
        parsed_result.append({
            'Interval': interval,
            'Transfer': transfer,
            'Bitrate': bandwith
        })
    return parsed_result
result, error = client(server_ip)
result_list = parser(result.decode())

if error:
    print(error)
else:
    for value in result_list:
        if value['Transfer'] > 2 and value['Bitrate'] > 20:
            print(value)