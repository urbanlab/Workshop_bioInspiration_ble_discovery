from bluepy.btle import Scanner

#Declare global variables and create files
ble_devices = {}
ble_device = {}
deviceId = 0
scanner = Scanner()
devicesToSort = []
jsonDevices = "static/devices.json"

#Create a Json with all the devices during one scan (erases the previous Json)
while True : 

    #Declare loop variables and begin scan
    
    devices = scanner.scan(3.0)
    deviceId = 0

    #For each device found, write the device in the Json and filter the first one by the signal strenght
    for device in devices:

        #Count the number of iterations
        deviceId = deviceId + 1

        #Write each the Json line and replace ' with " for correct formatting
        ble_device = {"adress": device.addr, "signal_strengh": device.rssi }
        #print(device.getScanData())
        
        # push the devices dict in an array to be able to sort them by signal strenght
        devicesToSort.append(ble_device)
        
        #Print to demonstrate you're a hacker
        print(ble_device)



    #Sort the devices by signal strenght
    devicesToSort.sort(key=lambda x: x['signal_strengh'], reverse=True)

    print(devicesToSort)
    with open(jsonDevices,'w') as f: 
            # replace single quotes with double quotes for correct formatting
            f.write(str(devicesToSort).replace("'", '"'))
            # Write each device in the Json
            #f.write(str(devicesToSort))
    f.close()


    exit()

    #Print the devices sorted by signal strenght
    for device in devicesToSort:
        with open(jsonDevices,'w') as f: 
            # Write each device in the Json
            f.write(str(device) + ",\n")
            # If the device is not the last one, write a comma
            if deviceId != len(devicesToSort):
                f.write(",")
                # Write a new line
                f.write("\n")
            else :
                f.write("]")
            f.close()
        

        
    #Erases the content of the Json
    print("#######################################################")
    with open(jsonDevices,'w') as f: 
        pass
    f.close()