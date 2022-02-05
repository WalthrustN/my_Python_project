# w writing a append r read only r+ read/write
#file = open("./data.csv", "r")

# print(file.read())
# this reads the whole file and prints it to the console

#for line in file:
#	print(line)
# Prints line by line in the file

#print(file.readlines())
# prints all characters in the file even new line.
#file.close()


#*** Preferred method for opening files because it automatcally closes
# them.
import os.path

filename = "data.csv"

if os.path.isfile(filename):
	with open(filename, "r") as file:
		print(file.read())
	
else:
	print(f"The {filename} does not exist!")


