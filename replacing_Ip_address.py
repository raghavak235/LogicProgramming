# Defanging an IP address
# Given a valid IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period '.' with "[.]".
# input ----------> A string
# constraint -----> non-empty String
# output ---------> replacement String


def ip_address_replacement():
    ip_addr = input()
    print(ip_addr.replace(',','[.]'))