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
	print b
	while (subf > 0):
		print(subf)
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
						print(bin_b[x])
						print(bin_c[x])
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


print(isSubnetValid("123.123.123.123/32","123.123.123.123"))