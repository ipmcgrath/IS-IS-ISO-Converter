# IS-IS ISO Converter

I wrote this script for our operations team to easily convert between loopback ISO addresses for IS-IS and the loopback's IPv4 address. 

## Usage

`./isis-iso.py [ ip2iso ipv4address | iso2ip isoaddress`

## Examples

Converting loopback IPv4 address 192.0.2.100:
```
cjones@cjones-mbp$ ./isis-iso.py ip2iso 192.0.2.100

=====================================================
isis-iso.py
Converts IPv4 address to NSAP ISO address or
NSAP ISO address to IPv4 address.
Assumes AFI 49 Area 0001 and NSEL 00
=====================================================

IP address 192.0.2.100 produces ISO address:
49.0001.1920.0000.2100.00

set interfaces lo0 unit 0 family iso address 49.0001.1920.0000.2100.00
```

Converting 49.0001.1920.0000.2100.00 to an IPv4 address:
```
cjones@cjones-mbp$ ./isis-iso.py iso2ip 49.0001.1920.0000.2100.00

=====================================================
isis-iso.py
Converts IPv4 address to NSAP ISO address or
NSAP ISO address to IPv4 address.
Assumes AFI 49 Area 0001 and NSEL 00
=====================================================

ISO address 49.0001.1920.0000.2100.00 produces IP address:
192.0.2.100
```