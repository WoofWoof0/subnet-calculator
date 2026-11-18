#function that runs an algorithm to convert decimal to binaries.
def octet_to_binary(octet):
    list = []
    listReturn = []

    if octet != 0:
        #the loop will get the remainder from the integer until the integer no longer 
        #can be divied by 2
        while octet != 0 :
            list.append(octet%2)
            octet = octet//2

        #check whether if the remainder output are 8 decimals numbers,
        #if it is, it will append the digits into the new List FILO style.
        if len(list) == 8:    
            while len(listReturn) != 8:
                listReturn.append(list.pop())
        #else check the list that supposed to be return contains 8 digits or not
        #if the total digits suppose to be output is not equal to 8 then integer
        #0 will be append into the return list, the the digits will be transfer 
        #into the return list from the result list FILO style.
        else:
            while len(listReturn) != 8:
                while len(list) + len(listReturn) != 8:
                    listReturn.append(0)
                listReturn.append(list.pop())

    #else if the octet is 0, then integer 0 will be append into the return list
    else:
        while len(listReturn) != 8:
            listReturn.append(0)

    return listReturn

#Funtion that takes in prefix number (e.g.24) and turn it into 32 bits mask bits.
#Example : /24 prefix will be 11111111 11111111 11111111 00000000 in 32 bits mask.
def prefix_to_mask(prefix):
    #checks whether the prefix is an integer numbers.
    try:
        prefix = int(prefix)

    #throw an execption error if the prefix is not integer and end the function.
    except ValueError:
        print("Error! Please re-enter the value!")
        return

    #create a new list to store the 32 bits mask.
    newIP = []
    #Note: a correct prefix should be between 0 to 32.
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
    #a new list that used to hold the new decimals, once the ipaddress is converted.
    v = []

    if len(splitedIP) != 4 :
        print("Incorrect IP Address!")
        return

    try:
        #map() fucntion is used to convert the digits into integer 
        splitedIP = list(map(int, splitedIP))
    #if map() function failed to convert the digits into integer an exception error will be prompted.
    except ValueError:
        print("IP Address has to be all in digits!")
        return

    #This loop checks every int on the list, making sure it is in the range.
    for i in splitedIP:
        if not (0 <= i <= 255):
            print("Incorrect IP Address!")
            return
        v.extend(octet_to_binary(i))
    
    return v

#Function that computes the network address by ANDing the IP with the mask 
#- Keeps the network bits, zeroes the host bits.
def network_address(ip_bits, mask_bits):
    #a list that store the result of the bitwise AND.
    list_return = []

    for i in range(0,32):
        if ip_bits[i] == 1 and mask_bits[i] == 1:
            list_return.append(1)
        else:
            list_return.append(0)
    return list_return

#Function that computes the network address - keeps the network bits,
#set the host bits to 1(the mirror of the network address).
def broadcast_address(ip_bits, mask_bits):
    list_return = []

    for i in range(0,32):
        if ip_bits[i] == 0 and mask_bits[i] == 1:
            list_return.append(0)
        else:
            list_return.append(1)

    return list_return

#Counts usable hosts: 2^(host bits) − 2, with special cases for /31 and /32.
def host_count(mask_bits):
    count = 0 

    for i in mask_bits:
        if i == 0:
            count+=1

    if count == 0:
        return 1
    elif count == 1:
        return 2
    else:
        return (2**count)-2

#A function that convert the Binary back into Decimal.
def bits_to_number(bits):
    bit = list(reversed(bits))
    return_int = 0

    for i in range(len(bit)):
        return_int += bit[i] * (2**i)

    return return_int

#A function that convert numbers into 32-bits binaries.
def number_to_bits(number):
    return_list = []

    #runs a while loop to get the binary result.
    while number != 0:
        return_list.append(number%2)
        number = number//2

    #32-bits check, adds 0 to the end to make up 32-bits if it's under 32bits.
    while len(return_list) < 32:
        return_list.append(0)
    return_list.reverse()

    return return_list

#A function convert 32-bits into ip address.
def bits_to_ip(bits):
    ans = []

    #slicing through the index every 8 int.
    for i in range(0,32,8):
        octet_ans = bits[i:i + 8]
        ans.append(str(bits_to_number(octet_ans)))
    return ".".join(ans)
    
ip = checkIP("192.168.1.10")
prefix = prefix_to_mask(24)
network = network_address(ip,prefix)
broadcast = broadcast_address(ip,prefix)
first_usable = bits_to_number(network) + 1
last_usable = bits_to_number(broadcast) - 1

ip2 = checkIP("10.0.0.0")
prefix2 = prefix_to_mask(8)
network2 = network_address(ip2,prefix2)
broadcast2 = broadcast_address(ip2,prefix2)
first_usable2 = bits_to_number(network2) + 1
last_usable2 = bits_to_number(broadcast2) - 1

ip3 = checkIP("172.16.5.4")
prefix3 = prefix_to_mask(26)
network3 = network_address(ip3,prefix3)
broadcast3 = broadcast_address(ip3,prefix3)
first_usable3 = bits_to_number(network3) + 1
last_usable3 = bits_to_number(broadcast3) - 1

print("IP Address: \t", bits_to_ip(ip))
print("Network: \t",bits_to_ip(network))
print("Broadcast: \t",bits_to_ip(broadcast))
print("Usable Range: \t",bits_to_ip(number_to_bits(first_usable))," - ",bits_to_ip(number_to_bits(last_usable)))
print("Usable Hosts: \t", host_count(prefix))

print("\nIP Address: \t", bits_to_ip(ip2))
print("Network: \t",bits_to_ip(network2))
print("Broadcast: \t",bits_to_ip(broadcast2))
print("Usable Range: \t",bits_to_ip(number_to_bits(first_usable2))," - ",bits_to_ip(number_to_bits(last_usable2)))
print("Usable Hosts: \t", host_count(prefix2))

print("\nIP Address: \t", bits_to_ip(ip3))
print("Network: \t",bits_to_ip(network3))
print("Broadcast: \t",bits_to_ip(broadcast3))
print("Usable Range: \t",bits_to_ip(number_to_bits(first_usable3))," - ",bits_to_ip(number_to_bits(last_usable3)))
print("Usable Hosts: \t", host_count(prefix3))