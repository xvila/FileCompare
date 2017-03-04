#This script compares two file directories and sets the file names and 
#file size as keys for the comparison.

import os
import Tkinter, tkFileDialog, tkMessageBox
import ttk

# GUI
root = Tkinter.Tk()
root.withdraw()

# blank dictionaries
originalDict = {}
newDict = {}

# Prompt user to select directories
currentDirectory = tkFileDialog.askdirectory(title='Please select original file directory') 
newDirectory = tkFileDialog.askdirectory(title='Please select new file directory')


#Create a dictionary of the original file directory
for (dirname, dirs, files) in os.walk(currentDirectory):
	for filename in files:
		thefile = os.path.join(dirname,filename)
		filesize = os.path.getsize(thefile)
		origKey = filename + str(filesize)
		originalDict[origKey] = thefile

#Create a dictionary for the new file directory
for (dirname, dirs, files) in os.walk(newDirectory):
	for filename in files:
		thefile = os.path.join(dirname,filename)
		filesize = os.path.getsize(thefile)
		newKey = filename + str(filesize)
		newDict[newKey] = thefile

#Compare two dictionaries and delete any values with matching keys
for key in originalDict.keys():
	if newDict.has_key(key):
		os.remove(newDict.get(key))

print tkMessageBox.showinfo("Done!", "This has been completed!")
