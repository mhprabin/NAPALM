import json
from napalm.base import get_network_driver
import pprint

optional_args = {'transport': 'https'}
driver = get_network_driver('eos')
dev = driver(hostname='192.168.1.2', username='prabin', password='prabin1234', optional_args=optional_args)
dev.open()
a= dev.get_facts()
print (a['hostname'])
print (a['os_version'])

with dev as eos:
    pprint.pprint(eos.compliance_report("validate-eos.yml"))

dev.close()
