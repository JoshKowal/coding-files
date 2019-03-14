import csv
import numpy
import datetime
import matplotlib.pyplot as plt
import pylab

def read_file(filename):
	"""
	Input: A string representing the name of the file to be read.

	Returns: Four lists, one containing the timestamps and the other three containing
	the voltages of each of the three panels. Indicies correspond to the same sample.
	"""
	#Initialize the sequences containing the times and voltages for each panel.
	times = []
	panel_f = []
	panel_g = []
	panel_h = []
	panel_i = []
	with open(filename, 'rb') as f:
		read = csv.reader(f, delimiter = ' ', quotechar = ' ')
		for row in read:
			s = ''
			for item in row:
				s = s + item
			data = s.split()
			#Uncomment line 28 below only if the compiler throws an error on line 22
			#print data
			#Create the lists of data - serial printing is buggy, hence the try except clause
			try:
				for i in range(0,len(data)):
					val = float(data[i])
					data[i] = val
				times.append(data[0])
				panel_f.append(data[1])
				panel_g.append(data[2])
				panel_h.append(data[3])
				panel_i.append(data[4])
				#Uncomment lines 41-42 below only if compiler throws an error on line 22;
				#Change x to the value of the first floating point number in the last line 
				#if times[-1] == x:
				#	break
			except ValueError:
				if data[0] is type(str):
					times = []
					panel_f = []
					panel_g = []
					panel_h = []
					panel_i = []
	return times, panel_f, panel_g, panel_h, panel_i

def generate_graph(filename):
	"""
	Input: The name of the file to be read.

	Returns: Nothing. Instead, this function generates a time graph to save to your
	computer.
	"""
	times, f, g, h, i = read_file(filename)
	#Format is datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo) - all are optional
	#I use datetime.datetime(year, month, day, hour, minute, second)
	custom_date = datetime.datetime(2018, 7, 17, 12, 32, 04) #Remember what time you started the Arduino code

	#This is for one day's worth of data - if the test runs multiple days, refer to CSVtoGraphSolarTest1_3.py
	#on how to account for multiple days and how to generate multiple graphs for multiple days.

	#Line below gets the actual time of day when that measurement was recorded
	t = [custom_date + datetime.timedelta(milliseconds = x) for x in times]
	
	#Add as many plots as needed using this format:
	f1 = plt.figure() #Create new plot
	#Plot lines, title graph, and label axes
	#To plot, use plt.plot(x, y, color, label)
	plt.plot(t, f, color = 'red', label = 'Panel F Voltage')
	plt.plot(t, g, color = 'blue', label = 'Panel G Voltage')
	plt.plot(t, h, color = 'green', label = 'Panel H Voltage')
	plt.plot(t, i, color = 'yellow', label = 'Panel I Voltage')
	plt.xlabel('Time of Day')
	plt.ylabel('Voltage (V)')
	plt.title('Voltage vs Time of Day: (Day of Trial)')
	#Create a legend
	legend = plt.legend(fontsize = 'small', loc = 'lower left')
	
	plt.show()

#Uncomment below and replace 'name_of_file' with the name of the CSV file
#generate_graph('name_of_file.csv')
