import minimalmodbus
import serial
import time

registers = {
    "Grid Voltage": {'register':4502, 'multiplier':0.1, 'unit':'V'},
    "Grid Current": {'register':532, 'multiplier':0.1, 'unit':'A'},
    
    "Ambient Temperature": {'register':546, 'multiplier':0.1, 'unit':'C'},

    "PV Temperature": {'register':544, 'multiplier':0.1, 'unit':'C'},
    "Solar Voltage": {'register':263, 'multiplier':0.1, 'unit':'V'},
    "Solar Current": {'register':548, 'multiplier':0.1, 'unit':'A'},
    "Solar Power": {'register':265, 'multiplier':1, 'unit':'W'},
    
    "Battery Voltage": {'register':257, 'multiplier':0.1, 'unit':'V'},
    "Battery Current In": {'register':0, 'multiplier':1, 'unit':'A'},
    "Battery Power In": {'register':270, 'multiplier':0.1, 'unit':'W'},
    "Battery Current Out": {'register':0, 'multiplier':0.1, 'unit':'A'},
    "Battery Power Out": {'register':0, 'multiplier':1, 'unit':'W'},
    
    "Inv Temperature": {'register':545, 'multiplier':0.1, 'unit':'C'},
    "Inv Current": {'register':537, 'multiplier':0.1, 'unit':'A'},
    "Inv Voltage": {'register':534, 'multiplier':0.1, 'unit':'V'},
    "Inv VA": {'register':540, 'multiplier':1, 'unit':'VA'},
    "Inv Power": {'register':539, 'multiplier':1, 'unit':'W'}
}

if __name__ == "__main__":
    powerMeter = minimalmodbus.Instrument('/dev/ttyUSB0', 0x05)
    powerMeter.serial.baudrate = 2400
    #powerMeter.serial.bytesize = 8
    powerMeter.serial.parity = serial.PARITY_NONE
    #powerMeter.serial.stopbits = 1
    powerMeter.serial.timeout = 3
    powerMeter.mode = minimalmodbus.MODE_RTU
    #powerMeter.strict = False 
    print('Details of the power meter are:')
    print(powerMeter)
    
    try:
        #for register in range(500, 504):
        register = powerMeter.read_register(4502)  # Function code 3 for reading
        print("Grid Voltage:", register/10)
        register = powerMeter.read_register(4505)  # Function code 3 for reading
        print("Charging:", register)
        register = powerMeter.read_register(4503)  # Function code 3 for reading
        print("Freq:", register/10)
        register = powerMeter.read_register(4538)  # Function code 3 for reading
        print("Voltage Current Ragne:", register)
    except Exception as e:
        print(e)