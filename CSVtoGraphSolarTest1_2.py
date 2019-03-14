import csv
import matplotlib.pyplot as plt
import pylab
import numpy
import datetime

def read_file(filename):
	"""
	Input: A string representing the name of the file to be read.

	Returns: Four lists, one containing the timestamps and the other three containing
	the voltages of each of the three panels. Indicies correspond to the same sample.
	"""
	#Initialize the sequences containing the times and voltages for each panel
	times = []
	panel_a = []
	panel_b = []
	panel_c = []
	with open(filename, 'rb') as f:
		read = csv.reader(f, delimiter = ' ', quotechar = ' ')
		for row in read:
			s = ''
			for item in row:
				s = s + item
			data = s.split()
			#Uncomment line 27 below only if the compiler throws an error on line 21
			#print data
			#Create the lists of data - serial printing is buggy, hence the try except clause
			try:
				for i in range(0,len(data)):
					val = float(data[i])
					data[i] = val
				times.append(data[0])
				panel_a.append(data[1])
				panel_b.append(data[2])
				panel_c.append(data[3])
				#Uncomment lines 39-40 below only if the compiler throws an error on line 21; replace x with the 
				#value of the first floating point number in the last line
				if times[-1] == 126698270:
					break
			except ValueError:
				try:
					if data[0] is type(str):
						times = []
						panel_a = []
						panel_b = []
						panel_c = []
				except:
					break
	return times, panel_a, panel_b, panel_c

def generate_graph(filename):
	"""
	Input: A string representing the name of the file to be read.

	Returns: Nothing. Instead, this function generates a line graph to save to your
	computer.
	"""
	times, panel_a, panel_b, panel_c = read_file(filename)
	#Format is datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo) - all are optional
	#I use datetime.datetime(year, month, day, hour, minute, second)
	startdate = datetime.datetime(2018, 7, 5, 13, 20, 2) #Remember what time you started the Arduino code
	#Create more splitdates depending on how many days you run the trial
	#No need for a splitdate if the test is all in the same day
	splitdate = datetime.datetime(2018, 7, 6, 0, 0, 0)
	
	#Create the lists which will be graphed below
	#Add code in same format depending on how many days you run the trial - below is for two days
	#Don't run lines 70-95 if testing takes place on the same day
	dates1 = []
	dates2 = []
	
	a1 = []
	b1 = []
	c1 = []
	
	a2 = []
	b2 = []
	c2 = []
	
	count = 0
	for t in times:
		x = startdate + datetime.timedelta(milliseconds = t) #Gets the actual time of day when that measurement was recorded
		if x < splitdate: #Check if this is on day 1
			dates1.append(x)
			a1.append(panel_a[count])
			b1.append(panel_b[count])
			c1.append(panel_c[count])
			count += 1
		else: #In this case, this means that day 2 is the final day of testing
			dates2.append(x)
			a2.append(panel_a[count])
			b2.append(panel_b[count])
			c2.append(panel_c[count])
			count += 1

	#dates = [startdate + datetime.timedelta(milliseconds = t) for t in times] #Uncomment this line only if lines 70-95 were not run
	#Add as many plots as needed using this format:
	f1 = plt.figure() #Create new plot
	#Plot lines, title graph, and label axes
	#To plot, use plt.plot(x, y, color, label) and use dates for the x value if lines 70-95 were not run
	plt.plot(dates1, a1, color = 'red', label = 'Panel A Voltage')
	plt.plot(dates1, b1, color = 'blue', label = 'Panel B Voltage')
	plt.plot(dates1, c1, color = 'green', label = 'Panel C Voltage')
	plt.xlabel('Time of Day')
	plt.ylabel('Voltage (V)')
	plt.title('Voltage vs. Time of Day: (Day of Trial)')
	#Create a legend
	legend = plt.legend(fontsize = 'small') #Add a loc variable to change the location of the legend

	#Creating this plot below is not necessary if the test is all in the same day
	f2 = plt.figure() #Creates a fresh plot
	plt.plot(dates2, a2, color = 'red', label = 'Panel A Voltage')
	plt.plot(dates2, b2, color = 'blue', label = 'Panel B Voltage')
	plt.plot(dates2, c2, color = 'green', label = 'Panel C Voltage')
	plt.xlabel('Time of Day')
	plt.ylabel('Voltage (V)')
	plt.title('Voltage vs. Time of Day: (Day of Trial)')
	legend2 = plt.legend(fontsize = 'small', loc = 'upper left') #loc is the location of the legend

	plt.show()

#Uncomment below and replace 'name_of_file' with the name of the CSV file
#generate_graph('name_of_file.csv')
