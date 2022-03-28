from bluepy.btle import Scanner

ble_devices = {}
ble_device = {}

while True : 
    f = open("devices.json", "a")
    scanner = Scanner()
    devices = scanner.scan(3.0)
    f.write("[\n")
    for device in devices:
        #print("DEV = {} RSSI = {}".format(device.addr, device.rssi))
        #print(device.getScanData())

        # Get device infos plus name if ther is one
        #print(str(device.addr) + " " + str(device.rssi) + " " + str(device.getScanData()))

        # Get device infos plus name if ther is one
        #print(str(device.addr) + " " + str(device.rssi))
        ble_device = str({"adress": device.addr, "signal_strengh": device.rssi }).replace("'", '"')
        print(ble_device)
        f.write(ble_device)
        f.write(",\n")
    f.write("]")

    print("#######################################################")
    with open("devices.json",'w') as f: 
        pass
    f.close()

