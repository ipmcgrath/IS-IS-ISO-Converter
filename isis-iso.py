#!.venv/bin/python

import ipaddress
import sys
import re

def ip_to_iso(ip):
    octets = ip.split('.')
    filled = octets[0].zfill(3) + octets[1].zfill(3) + octets[2].zfill(3) + octets[3].zfill(3)
    iso = '49.0001.' + '.'.join(filled[i:i+4] for i in range(0, len(filled), 4)) + '.00'
    return iso

def iso_to_ip(iso):
    octets = iso.split('.')
    merged = octets[2] + octets[3] + octets[4]
    ip = '.'.join(merged[i:i+3] for i in range(0, len(merged), 3))
    ip = str(ipaddress.ip_address(ip))
    return ip

def main():

    print("""
=====================================================
isis-iso.py
Converts IPv4 address to NSAP ISO address or
NSAP ISO address to IPv4 address.
Assumes AFI 49 Area 0001 and NSEL 00
=====================================================
""")

    if len(sys.argv) == 3 and sys.argv[1] == 'ip2iso':
        try:
            network = ipaddress.IPv4Network(sys.argv[2])
            iso = ip_to_iso(sys.argv[2])
            print('IP address ',sys.argv[2],' produces ISO address:\n', iso, '\n', sep='')
            print('set interfaces lo0 unit 0 family iso address', iso, '\n')
        except ValueError:
            print('Not a valid IPv4 Address:', sys.argv[2], '\n')

    elif len(sys.argv) == 3 and sys.argv[1] == 'iso2ip':

        try:
            regex = re.compile('^49\.0001\.\d{4}\.\d{4}\.\d{4}\.00$')
            if regex.match(sys.argv[2]):
                ip = iso_to_ip(sys.argv[2])
                print('ISO address ',sys.argv[2],' produces IP address:\n', ip, '\n', sep='')
            else:
                raise ValueError 
        except ValueError:
            print('Not a valid Sempra ISO Address:', sys.argv[2], '\n')

    else:

        print('USAGE: ./isis-iso.py [ ip2iso ipv4address | iso2ip isoaddress ]\n')

if __name__ == '__main__':
    main()
exit()