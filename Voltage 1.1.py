import matplotlib.pyplot as plt
import pylab
import numpy

#Note: This is an outdated program. This uses .txt files, so it is advised to use
#the other programs, which read CSV files.

def read_file(filename):
	"""
	Input: string representing the name of a text file.

	Returns: A list containing three elements. Each element is a dictionary of the voltages
	associated with each panel for each sample taken.
	"""
	panel_a = {}
	panel_b = {}
	panel_c = {}
	acount = 0
	bcount = 0
	ccount = 0
	f = open(str(filename), "r")
	#print f -- for debugging purposes
	count = 0
	#Read the text file and sort the voltages for all three panels
	for line in f:
		count += 1
		if count > 1860:
			break
		words = line.split()
		voltage = float(words[1])
		if words[0][0] == 'A' or (words[0][0] != 'B' and words[0][0] != 'C'):
			panel_a[acount] = voltage
			acount += 1
		elif words[0][0] == 'B':
			panel_b[bcount] = voltage
			bcount += 1
		elif words[0][0] == 'C':
			panel_c[ccount] = voltage
			ccount += 1
	#return count -- for debugging purposes; make sure an equal number of data
	#points for each are read
	return [panel_a, panel_b, panel_c]

def generate_graph(filename):
	"""
	Inputs: The name of the text file.

	Returns: Nothing. Graphs will appear as the program runs.
	"""
	data = read_file(filename)
	#Get sample numbers
	t = range(0,len(data[0]))
	#Plot the data for each panel, where the data is stored in the dictionary
	#Format is plt.plot(x-values, y-values, color, label)
	plt.plot(t, data[0].values(), color = 'red', label = 'Panel A Voltage')
	plt.plot(t, data[1].values(), color = 'blue', label = 'Panel B Voltage')
	plt.plot(t, data[2].values(), color = 'green', label = 'Panel C Voltage')
	plt.xlabel('Sample')
	plt.ylabel('Voltage')
	plt.title('Your Title Here')
	legend = plt.legend(fontsize = 'x-small') #Creates a legend
	plt.show()

#If the files and program are in your desktop folder, uncommment below and run
#to see the graphs

#generate_graph("ABC.txt")
#generate_graph("ACB.txt")
#generate_graph("CAB.txt")
#generate_graph("CBA.txt")
#generate_graph("BCA.txt")
#generate_graph("BAC.txt")
