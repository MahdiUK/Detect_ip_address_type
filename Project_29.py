def detect_ip_address_type(ip_address):
    # Split the IP address into octets
    octets = ip_address.split(".")
    
    # Check if the IP address is classful or classless
    if int(octets[0]) < 128:
        return "Class A (Classful)"
    elif int(octets[0]) < 192:
        return "Class B (Classful)"
    elif int(octets[0]) < 224:
        return "Class C (Classful)"
    elif int(octets[0]) < 240:
        return "Class D (Multicast)"
    elif int(octets[0]) < 256:
        return "Class E (Experimental)"
    else:
        # Check if the IP address is classless
        for octet in octets:
            if int(octet) < 0 or int(octet) > 255:
                return "Invalid IP address"
        return "Classless"
    
# Ask the user to enter an IP address
ip_address = input("Enter an IP address: ")

# Detect the type of the IP address and print the result
ip_address_type = detect_ip_address_type(ip_address)
print(f"The IP address {ip_address} is {ip_address_type}.")