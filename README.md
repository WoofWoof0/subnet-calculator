# subnet-calculator

A collectives of functions that calculate subnet information from an IPv4 address and prefix. Built from scratch, to serves the purpose of understanding how the subnetting works at the bits level.

## WHAT DOES IT DO?

Takes an IP address and a CIDR prefix (e.g. '192.168.1.10/24'), it calculate out the network address, broadcast address, the range of usuable host address and the numbers of the host the subnet can hold. Every algorithm: the binary conversion, subnet masking, and the bitwise operations - is implement by hand rather than using built-in functions from python.

## EXAMPLE

IP Address:      192.168.1.10
Network:         192.168.1.0
Broadcast:       192.168.1.255
Usable Range:    192.168.1.1  -  192.168.1.254
Usable Hosts:    254

IP Address:          10.0.0.0
Network:             10.0.0.0
Broadcast:           10.255.255.255
Usable Range:        10.0.0.1  -  10.255.255.254
Usable Hosts:        16777214

IP Address:          172.16.5.4
Network:             172.16.5.0
Broadcast:           172.16.5.63
Usable Range:        172.16.5.1  -  172.16.5.62
Usable Hosts:        62

## FEATURES

- Validates IPv4 addresses.
- Converts between decimal and binary.
- Builds the subnet mask from a CIDR prefix (/0 to /32).
- Calculates the network address (bitwise AND).
- Calculates the broadcast address.
- Calculates the usable host(s) range and host count.
- Able to handle CIDR prefix (/31 and /32).

## HOW IT WORKS

1. The IP address is validated and converted into 32-bits.
2. The prefix is turned into a subnet mask - a row of 1s (network bits) followed by 0s (host bits).
3. The network address is found with bitwise AND of the IP and the mask: where the mask is 1 the IP's bits passes through, and where the mask is 0 the bit become 0. This zeroes out the host part.
4. The broadcast address is the mirror of the network address - the host bits are set to 1 instead of 0.
5. The usuable range is the network address + 1 through the broadcast address - 1.
6. The usuable host count is the 2 power of the host bits minus 2. host count = (2**(host bits))-2

## WHY I BUILT IT THIS WAY

I deliberately avoided Python's 'ipadress' module, the goal of writting functions from scratch is to understand the how the subnetting works instead of just producing solutions.

## HOW TO RUN IT

Requires Python 3.

'''
python subnet_calc.py
'''

## WHAT I LEARNED 
1. How IP addressing and subnetting work at the binary level.
2. How subnet mask and the network/host split actually function.
3. Bitwise operations (AND OR) and why they're used in the networking.
4. Debugging real issue: integer vs float division, list mutation side effects, and off-by-one padding bugs.