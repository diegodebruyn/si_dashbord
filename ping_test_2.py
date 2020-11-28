import json
import os
with open('ip_list.json') as json_file:
    data = json.load(json_file)
    ip_list=data['ip_list']

for ip in ip_list:
    response=os.popen(f"ping {ip}").read()
    if "Received=4" in response:
        print(f"UP {ip} Ping Successful")
    else:
        print(f"DOWN {ip} Ping Failed")
