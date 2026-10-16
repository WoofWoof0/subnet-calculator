#function that runs an algorithm to convert decimal to binaries.
def octet_to_binary(octet):
    list = []
    listReturn = []

    if octet != 0:
        while octet != 0 :
            list.append(octet%2)
            octet = int(octet/2)

        if len(list) == 8:    
            while len(listReturn) != 8:
                listReturn.append(list.pop())
        else:
            while len(listReturn) != 8:
                while len(list) + len(listReturn) != 8:
                    listReturn.append(0)
                listReturn.append(list.pop())
    else:
        while len(listReturn) != 8:
            listReturn.append(0)

    return listReturn

def prefix_to_mask(prefix):
    try:
        prefix = int(prefix)

    except ValueError:
        print("Error! Please re-enter the value!")
        return

    newIP = []
    if not (0 <= prefix <= 32):
        print("Incorrect Prefix!")
        return
    else:
        for i in range(0,prefix):
            newIP.append(1)
        while len(newIP) != 32:
            newIP.append(0)

    return newIP

#Function that take in IP address as a parameter, checks and valify it and then convert it into binaries.
def checkIP(ipAdress):

    splitedIP = ipAdress.split(".")
    v = []

    if len(splitedIP) != 4 :
        print("Incorrect IP Address!")
        return

    try:
        splitedIP = list(map(int, splitedIP))
    except ValueError:
        print("IP Address has to be all in digits!")
        return

    for i in splitedIP:
        if not (0 <= i <= 255):
            print("Incorrect IP Address!")
            return
        v.extend(octet_to_binary(i))
    
    return v

def network_address(ip_bits, mask_bits):
    try:
        if type(ip_bits) == "list":
            for i in range(0,len(ip_bits)):
                ip_bits[i] = int(ip_bits[i])
        else:
            return
        if type(mask_bits) == "list":
            for i in range(0,len(mask_bits)):
                mask_bits[i] = int(mask_bits[i])
        else:
            return

    except ValueError:
        print("Error here!")
        return

    return ip_bits

print("network_address: ",network_address("192.168.1.0",-1))
