import netaddr
import json
import nmap
import pprint
import sys


def scan_network(network):
    result_list = dict()
    try:
        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sS')
        for host in nm.all_hosts():
            protocol = dict()
            for proto in nm[host].all_protocols():
                port_dict = dict()
                for port in nm[host][proto].keys():
                    port_dict[port] = nm[host][proto][port]['state']
                protocol[proto] = port_dict
            result_list[host] = protocol
        return result_list
    except:
        pass


def main():
    if sys.argv[1]:
        network = sys.argv[1]
    else:
        network = '127.0.0.1'
    result_list = scan_network(network)
    with open('result_nmap.json', 'w+') as fo:
        fo.write(json.dumps(result_list))
        fo.close()
    print(json.dumps(result_list, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
