import json
import requests
requests.packages.urllib3.disable_warnings()


api_url = "https://10.10.10.2/restconf/data/ietf-interfaces:interfaces/interface=Loopback11"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = ("Admin", "Admin123!")

new_loopback = {
    "ietf-interfaces:interface": {
        "name": "Loopback11",
        "description": "PYTHON Loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "3.3.3.3",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

resp = requests.put(api_url, data=json.dumps(new_loopback), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))






