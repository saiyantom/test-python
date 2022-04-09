ipadd = {'eth0': {'IP Address':'1.1.1.1', 'status':'up'},
         'eth1': {'IP Address':'2.2.2.2', 'status':'up'},
         'wlan0': {'IP Address':'3.3.3.3', 'status':'down'},
         'wlan1': {'IP Address':'4.4.4.4', 'status':'up'}
        }

status = ''
ipadd_up = {}

interface = input("Enter network interface: ")

if interface in ipadd.keys():
    status = ipadd[interface]['status']
else:
    status = 'Not Available'
print(f'Interface Status: {status}')

for iface,ip in ipadd.items():
    if ip['status'] == 'up':
        ipadd_tmp = { iface:ip['IP Address'] }
        ipadd_up.update(ipadd_tmp)

print(ipadd_up)

print(f'Number of interfaces: {len(ipadd.keys())}\n')

ifkeys = ['eth2', 'wlan2']
ifvalues = [ {'IP Address':'5.5.5.5', 'status':'up'},
             {'IP Address':'7.7.7.7', 'status':'down'} ]

ipadd.update(zip(ifkeys, ifvalues))

print(f'All Network Interface: {ipadd}')
