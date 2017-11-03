#!/usr/bin/env python

import socket

def recv_until(conn, str):
	buf = ''
	while not str in buf:
		buf += conn.recv(1)
	return buf

def getValidSubnet(host):
	a = host.split(".")
	return (a[0]+"."+a[1]+"."+a[2]+"."+"0"+"/"+"24")

def countHosts(subnet):
	a = subnet.split("/")
	return str(2**(32-int(a[1])))

def isSubnetValid(subnet, host):
	a = subnet.split("/")
	b = a[0].split(".")
	sub = int(a[1])
	subf = float(sub)/8
	c = host.split(".")
	total_byte = 0
	i = 0
	skor = 0
	while (subf > 0):
		if (bin(int(b[i]))[2:] == bin(int(c[i]))[2:]):
			skor += 8
		else:
			bin_b = bin(int(b[i]))[2:]
			bin_c = bin(int(c[i]))[2:]
			len_bin_b = len(bin_b)
			len_bin_c = len(bin_c)
			if (len_bin_b < len_bin_c):
				skor += 8-len_bin_c
			else:
				if (len_bin_c < len_bin_b):
					skor += 8-len_bin_b
				else:
					x = 0
					if (len_bin_b < 8):
						skor += 8-len_bin_b
					while (x<=len_bin_b):
						if(bin_b[x] == bin_c[x]):
							skor+=1
							x+=1
						else:
							break
		i+=1
		subf-=1

	if (skor >= sub):
		return "T"
	else :
		return "F"
	
TCP_IP = 'hmif.cf'
TCP_PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = recv_until(s, 'NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

data = recv_until(s, 'Verify NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

print recv_until(s, '\n')[:-1]

# Phase 1
for i in range(100):
	recv_until(s, 'Host: ')
	host = recv_until(s, '\n')[:-1]
	recv_until(s, 'Subnet: ')
	s.send(getValidSubnet(host) + '\n')
print recv_until(s, '\n')[:-1]

# Phase 2
for i in range(100):
	recv_until(s, 'Subnet: ')
	subnet = recv_until(s, '\n')[:-1]
	recv_until(s, 'Number of Hosts: ')
	s.send(countHosts(subnet) + '\n')
print recv_until(s, '\n')[:-1]

# Phase 3
for i in range(100):
	recv_until(s, 'Subnet: ')
	subnet = recv_until(s, '\n')[:-1]
	recv_until(s, 'Host: ')
	host = recv_until(s, '\n')[:-1]
	s.send(isSubnetValid(subnet, host) + '\n')
print recv_until(s, '\n')[:-1]

s.close()
