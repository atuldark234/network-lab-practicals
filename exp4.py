import ipaddress
n = ipaddress.ip_network(input("Enter network (e.g. 192.168.1.0/24): "), strict=False)
print("First IP:", n[0]); print("Last IP:", n[-1])
