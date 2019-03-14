import serial
import csv

ser = serial.Serial('/dev/ttyACM0', 9600) #Check port name which is first argument
#Port name should be '/dev/ttyACMx', where x is an integer, for Raspberry Pi
ser.flushInput()

#Note that this is an infinite loop; to end the program, unplug the Arduino or hit Ctrl-C
while True:
	try:
		serline1 = ser.readline().decode('utf-8')[:-1] #Necessary for graphing
		print serline1 #To see data, also for debugging purposes
		with open('your_file_name.csv', 'a') as f:
			writer = csv.writer(f, delimiter = ' ', quotechar = ' ')
			writer.writerow(serline1)
		f.close()
	except:
		print 'Error'
		break