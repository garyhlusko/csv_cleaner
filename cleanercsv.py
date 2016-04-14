import csv
import glob
import xlrd
import pickle

state_dict = pickle.load(open("C:\Python27/state_dict_py.txt"))
address_dict = pickle.load(open("C:\Python27/address_dict_py.txt"))
state_set = pickle.load(open("C:\Python27/state_dictset_py.txt"))
cleaned = []
junk = []


find_incomplete = ['and','&']

path1 = "C:\Users/valued/Desktop/politech/politech csv/*.csv"

def FindIncomplete(line):
	for item in line:
		if item == '' or item == ' ' or any(find_incomplete) in line:
			junk.append(line)
			return False
		else:
			return True
			
def state_abbreviations(line,column):
		if line[column].upper() in state_set:
			return True
		else:
			try:
				line[column] = state_dict[line[column].lower()] 
				return True
			except:
				return False
			
def zip(line,column):
		if type(int(line[column]))==int and len(str(line[column])) == 5:
			return True
		else:
			return False
			
for file in glob.glob(path1):
	with open(file) as csvfile:
		sniffer = csv.reader(csvfile, delimiter = ',')
		headers = sniffer.next()
		for line in sniffer:
			if FindIncomplete(line) and state_abbreviations(line,3) and zip(line,4) == True:
				cleaned.append(line)
			else:
				junk.append(line)	


path2 = "C:\Users/valued/Desktop/politech/politech csv/*.xlsx"

for excel in glob.glob(path2):
	book =  xlrd.open_workbook(excel)
	sheet = book.sheets()
	sheet = book.sheet_by_index(0)
	for sheet in book.sheets():  
		for row in range(sheet.nrows):    
			rowers = sheet.row_values(row)
			pass
		 