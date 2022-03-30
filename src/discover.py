from bluepy.btle import Scanner

#Declare global variables and create files
ble_devices = {}
ble_device = {}
deviceId = 0
scanner = Scanner()
jsonDevices = "static/devices.json"

#Create a Json with all the devices during one scan (erases the previous Json)
while True : 

    #Declare loop variables and begin scan
    f = open(jsonDevices, "a")
    devices = scanner.scan(3.0)
    deviceId = 0

    # Write the first line of the Json
    f.write("[\n")

    for device in devices:
        #print("DEV = {} RSSI = {}".format(device.addr, device.rssi))
        #print(device.getScanData())

        # Get device infos plus name if ther is one
        #print(str(device.addr) + " " + str(device.rssi) + " " + str(device.getScanData()))

        # Get device infos plus name if ther is one
        #print(str(device.addr) + " " + str(device.rssi))

        #Count the number of iterations
        deviceId = deviceId + 1

        #Write each the Json line and replace ' with " for correct formatting
        ble_device = str({"adress": device.addr, "signal_strengh": device.rssi }).replace("'", '"')
        #print(device.getScanData())
        moreData = device.getScanData()
        getDescription(adtype)
        try :
            print(moreData)
            #print(moreData[2])
            
        except :
            print("null")
        f.write(ble_device)

        #Add the correct fomating for each line ending (different for te last line)
        if deviceId == len(devices) :
            f.write("\n]")
        else :
            f.write(",\n")
        
        #Print to demonstrate you're a hacker
        print(ble_device)

    #Erases the content of the Json
    print("#######################################################")
    with open(jsonDevices,'w') as f: 
        pass
    f.close()
