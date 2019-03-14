import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import datetime
import numpy
import csv
import pylab

def read_file(filename):
	"""
	Input: A string representing the name of the file to be read.

	Returns: Three lists, one containing times in milliseconds since the recording
	started, one listing the recorded voltages, and one listing the recorded currents.
	"""
	#Initialize the sequences containing the times, voltages, and currents read by the Attopilot
	times_high_throttle = []
	voltages_high_throttle = []
	currents_high_throttle = []
	times_med_throttle = []
	voltages_med_throttle = []
	currents_med_throttle = []
	with open(filename, 'rb') as f:
		read = csv.reader(f, delimiter = ' ', quotechar = ' ')
		for row in read:
			s = ''
			for item in row:
				s = s + item
			data = s.split()
			#Uncomment line 26 below only if the compiler throws an error at line 20
			#print data
			#Create the lists of data - serial printing is buggy, hence the try except clause
			try:
				for i in range(1,len(data)):
					val = float(data[i])
					data[i] = val
				if data[0] == 'High': #Sort the data based on throttle level
					times_high_throttle.append(data[1])
					voltages_high_throttle.append(data[2])
					currents_high_throttle.append(data[3])
				if data[0] == 'Medium': #Sort the data based on throttle level
					times_med_throttle.append(data[1])
					voltages_med_throttle.append(data[2])
					currents_med_throttle.append(data[3])
				#Uncomment lines 46-47 below only if the compiler throws an error on line 24; replace x with the 
				#value of the first number in the last printed line and comment line 30 again
				#if times[-1] == x:
				#	break
			except ValueError:
				if data[0] is type(str):
					times = []
					voltages = []
					currents = []
	return times_high_throttle, voltages_high_throttle, currents_high_throttle, times_med_throttle, voltages_med_throttle, currents_med_throttle

def generate_graph(filename):
	"""
	Input: A string representing the name of the file to graph.

	Returns: Nothing. Instead, this function generates a graph to save to your computer.
	"""
	times_h, v_h, i_h, times_m, v_m, i_m = read_file(filename)
	#Format is datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo) - all are optional
	#I use datetime.datetime(year, month, day, hour, minute, second)
	start_date = datetime.datetime(2018, 7, 25, 13, 27, 24) #Remember what time you started the Arduino code

	#Below is for a one day test; for a two day test, uncomment the splitdate below
	#and sort the data similar to how I did in CSVtoGraphSolarTest1_3.py. You would need
	#two different lists for high throttle timestamps, high throttle voltages, high throttle
	#currents, medium throttle timestamps, medium throttle voltages, and medium throttle currents

	#Then, copy lines 75-88 and place above the plt.show() statement, and make any
	#adjustments to the legends and title as needed
	t_h = [start_date + datetime.timedelta(milliseconds = x) for x in times_h]
	t_m = [start_date + datetime.timedelta(milliseconds = y) for y in times_m]
	fig, ax1 = plt.subplots()
	ax1.set_xlabel('Time of Day')
	ax1.plot(t_h, v_h, color = 'red', marker = 'o', label = 'High Throttle Voltage')
	ax1.plot(t_m, v_m, color = 'blue', marker = 'o', label = 'Medium Throttle Voltage')
	ax1.set_ylabel('Voltage (V)')
	ax2 = ax1.twinx()
	ax2.plot(t_h, i_h, color = 'yellow', marker = 'o', label = 'High Throttle Current')
	ax2.plot(t_m, i_m, color = 'green', marker = 'o', label = 'Medium Throttle Current')
	ax2.set_ylabel('Current (A)')
	legend = ax1.legend(fontsize = 'x-small', loc = 'upper left')
	legend2 = ax2.legend(fontsize = 'x-small')
	legend.get_frame()
	legend2.get_frame()
	plt.title('Voltage And Current vs. Time of Day: (Day of Trial)')
	plt.show()

#Uncomment below and replace 'file_name_here' with the name of the CSV file when you are ready to generate a graph
#generate_graph('file_name_here.csv')