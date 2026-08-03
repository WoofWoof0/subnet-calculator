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
        v.append(octet_to_binary(i))
    
    return v

print(checkIP("192.168.1.0"))
