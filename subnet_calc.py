#function that runs an algorithm to convert decimal to binaries.
def octet_to_binary(octet):
    list = []
    listReturn = []

    if octet != 0:
        #the loop will get the remainder from the integer until the integer no longer 
        #can be divied by 2
        while octet != 0 :
            list.append(octet%2)
            octet = int(octet/2)

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

#Function that takes ip_bits and mask_bits and run through a bitwise AND equation.
def network_address(ip_bits, mask_bits):
    #a list that store the result of the bitwise AND.
    list_return = []

    for i in range(0,32):
        if ip_bits[i] == 1 and mask_bits[i] == 1:
            list_return.append(1)
        else:
            list_return.append(0)
    return list_return

def broadcast_address(ip_bits, mask_bits):
    list_return = []

    for i in range(0,32):
        if ip_bits[i] == 0 and mask_bits[i] == 1:
            list_return.append(0)
        else:
            list_return.append(1)

    return list_return
    
ip = checkIP("192.168.1.10")
prefix = prefix_to_mask(24)
print("network_address: ",network_address(ip,prefix))
print("broadcast_address: ",broadcast_address(ip,prefix))