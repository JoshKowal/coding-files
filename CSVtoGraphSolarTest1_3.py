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
	#Initialize the sequences containing the times and voltages for each panel.
	times = []
	panel_a = []
	panel_b = []
	panel_c = []
	panel_d = []
	panel_e = []
	with open(filename, 'rb') as f:
		read = csv.reader(f, delimiter = ' ', quotechar = ' ')
		for row in read:
			s = ''
			for item in row:
				s = s + item
			data = s.split()
			#Uncomment line 29 below only if the compiler throws an error on line 23
			#print data
			#Create the lists of data - serial printing is buggy, hence the try except clause.
			try:
				for i in range(0,len(data)):
					val = float(data[i])
					data[i] = val
				times.append(data[0])
				panel_a.append(data[1])
				panel_b.append(data[2])
				panel_c.append(data[3])
				panel_d.append(data[4])
				panel_e.append(data[5])
				#Uncomment lines 43-44 below only if compiler throws an error on line 23;
				#Change x to the value of the first floating point number in the last line 
				#if times[-1] == x:
				#	break
			except ValueError:
				if data[0] is type(str):
					times = []
					panel_a = []
					panel_b = []
					panel_c = []
					panel_d = []
					panel_e = []
	return times, panel_a, panel_b, panel_c, panel_d, panel_e

def generate_graph(filename):
	"""
	Input: A string representing the name of the file to be read.

	Returns: Nothing. Instead, this function generates a line graph to save to your
	computer.
	"""
	times, panel_a, panel_b, panel_c, panel_d, panel_e = read_file(filename)
	#Format is datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo) - all are optional
	#I use datetime.datetime(year, month, day, hour, minute, second)
	startdate = datetime.datetime(2018, 7, 9, 12, 40, 6) #Remember what time you started the Arduino code
	#Create more splitdates below depending on how many days you run the trial
	#No need for a splitdate if the test is all in the same day
	splitdate1 = datetime.datetime(2018, 7, 10, 0, 0, 0) 
	splitdate2 = datetime.datetime(2018, 7, 11, 0, 0, 0)

	#Create the lists which will be graphed below
	#Add code in same format depending on how many days you run the trial - below is for three days
	#Don't run lines 73-121 if testing takes place on the same day
	dates1 = []
	dates2 = []
	dates3 = []
	
	a1 = []
	b1 = []
	c1 = []
	d1 = []
	e1 = []
	
	a2 = []
	b2 = []
	c2 = []
	d2 = []
	e2 = []
	
	a3 = []
	b3 = []
	c3 = []
	d3 = []
	e3 = []
	
	count = 0
	for t in times:
		x = startdate + datetime.timedelta(milliseconds = t) #Gets the actual time of day when that measurement was recorded
		if x < splitdate1: #Check if this is on day 1
			dates1.append(x)
			a1.append(panel_a[count])
			b1.append(panel_b[count])
			c1.append(panel_c[count])
			d1.append(panel_d[count])
			e1.append(panel_e[count])
			count += 1
		elif x >= splitdate1 and x < splitdate2: #Check if this is on day 2
			dates2.append(x)
			a2.append(panel_a[count])
			b2.append(panel_b[count])
			c2.append(panel_c[count])
			d2.append(panel_d[count])
			e2.append(panel_e[count])
			count += 1
		else: #In this case, this means that day 3 is the final day of testing
			dates3.append(x)
			a3.append(panel_a[count])
			b3.append(panel_b[count])
			c3.append(panel_c[count])
			d3.append(panel_d[count])
			e3.append(panel_e[count])
			count += 1

	#dates = [startdate + datetime.timedelta(milliseconds = t) for t in times] #Uncomment this line only if lines 73-121 were not run
	#Add as many plots as needed using this format:
	f1 = plt.figure() #Create new plot
	#Plot lines, title graph, and label axes
	#To plot, use plt.plot(x, y, color, label) and use dates for the x value if lines 73-121 were not run
	plt.plot(dates1, a1, color = 'red', label = 'Panel A Voltage')
	plt.plot(dates1, b1, color = 'blue', label = 'Panel B Voltage')
	plt.plot(dates1, c1, color = 'green', label = 'Panel C Voltage')
	plt.plot(dates1, d1, color = 'orange', label = 'Panel D Voltage')
	plt.plot(dates1, e1, color = 'purple', label = 'Panel E Voltage')
	plt.xlabel('Time of Day')
	plt.ylabel('Voltage (V)')
	plt.title('Voltage vs. Time of Day: (Day of Trial)')
	#Create a legend
	legend = plt.legend(fontsize = 'small') #Add a loc variable to change the location of the legend
	
	#Creating these two plots below is not necessary if the test is all in the same day
	f2 = plt.figure() #Creates a fresh plot
	plt.plot(dates2, a2, color = 'red', label = 'Panel A Voltage')
	plt.plot(dates2, b2, color = 'blue', label = 'Panel B Voltage')
	plt.plot(dates2, c2, color = 'green', label = 'Panel C Voltage')
	plt.plot(dates2, d2, color = 'orange', label = 'Panel D Voltage')
	plt.plot(dates2, e2, color = 'purple', label = 'Panel E Voltage')
	plt.xlabel('Time of Day')
	plt.ylabel('Voltage (V)')
	plt.title('Voltage vs. Time of Day: (Day of Trial)')
	legend = plt.legend(fontsize = 'small', loc = 'upper left')
	
	f3 = plt.figure()
	plt.plot(dates3, a3, color = 'red', label = 'Panel A Voltage')
	plt.plot(dates3, b3, color = 'blue', label = 'Panel B Voltage')
	plt.plot(dates3, c3, color = 'green', label = 'Panel C Voltage')
	plt.plot(dates3, d3, color = 'orange', label = 'Panel D Voltage')
	plt.plot(dates3, e3, color = 'purple', label = 'Panel E Voltage')
	plt.xlabel('Time of Day')
	plt.ylabel('Voltage (V)')
	plt.title('Voltage vs. Time of Day: (Day of Trial)')
	legend = plt.legend(fontsize = 'small', loc = 'upper left')
	
	plt.show()

#Uncomment below and replace 'name_of_file' with the name of the CSV file
#generate_graph('name_of_file.csv')
