import serial
import datetime
import csv

ser = serial.Serial('/dev/ttyACM0', 9600) #Check port name which is first argument
#Port name should be '/dev/ttyACMx', where x is an integer, for Raspberry Pi
ser.flushInput()

running = False #For when the motor isn't running during the day
sleep_time = False #For when it is night and the motor won't run at all

#Note that this program is an infinite loop; to end the program, hit Ctrl-C.
try:
	while True:
		#Get the current date and the current hour and minute
		d = datetime.datetime.now()
		h = d.hour
		m = d.minute

		#Verify that it is during the daytime
		if not sleep_time or h == 7:
			#Turn on motor if the minutes is within the first 5 minutes of every
			#15 minutes
			if m % 15 < 5 and not running and h < 20:
				if ser.isOpen():
					print ser.isOpen()
					running = True
					ser.write('0'.encode('utf-8'))
			#Turn off motor if the time is outside the time intervals listed above
			if m % 15 >= 5 and running:
				if ser.isOpen():
					print ser.isOpen()
					running = False
					ser.write('0'.encode('utf-8'))
			#Read serial data and write the CSV file from serial data if motor is on
			#Arduino will only measure and print serial data when the motor is running
			if running:
				try:
					serline1 = ser.readline().decode('utf-8')[:-1] #Necessary for graphing
					print serline1 #To see data, also for debugging purposes
					with open('your_file_name.csv','a') as f:
						writer = csv.writer(f, delimiter = ' ', quotechar = ' ')
						writer.writerow(serline1)
					f.close()
				except:
					pass
		#Check if it is nighttime and the motor needs to stop running for the day
		if h < 7 or h >= 20:
			sleep_time = True
		else:
			sleep_time = False
except:
	print "Error"