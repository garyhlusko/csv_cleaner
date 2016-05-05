import csv
import glob
import xlrd
import pickle

state_dict = pickle.load(open("C:\Python27/state_dict_py.txt"))
address_dict = pickle.load(open("C:\Python27/address_dict_py.txt"))
state_set = pickle.load(open("C:\Python27/state_dictset_py.txt"))
cleaned = []
junk = []
find_incomplete_list = ['and','&']



class Csvcleaner():

	
	def __init__(self,addresses,state,zip,name = [],required=[],address_split=False,address_join=False,name_split=False,name_join=False):
		if required == None:
			required = []
		if name == None:
			name - []
		if addresses == None:
			addresses = []
		if address_join == None:
			address_join = False
		if address_split == None:
			address_split = False
		if name_split ==None:
			name_split = False
		if name_join == None:
			name_join= False
			
		self.addresses = addresses
		self.state = state
		self.zip = zip
		self.required = required
		self.addresses = addresses
		self.address_join = address_join
		self.address_split = address_split
		self.name = name
	
	
	def find_blanks(self,line):
	
		if self.required == []:
			for column in line:
				if column == '' or column == ' ':
					return False
				else:
					return True
		else:
			print required
			for column in required:
				item = line[column]
				if item == '' or item == ' ':
					return False
				else:
					return True
					
	def find_incomplete(self,line):
			if any(incomplete == line[self.addresses] for incomplete in find_incomplete_list):
				return False
			else:
				return True
				
	def state_abbreviations(self,line):
			if line[self.state].upper() in state_set:
				return True
			else:
				try:
					line[self.state] = state_dict[line[column].lower()] 
					return True
				except:
					return False
				
	def zip_scrub(self,line):
			if type(int(line[self.zip]))==int and len(str(line[self.zip])) == 5:
				return True
			else:
				return False

	def address_joiner(self,line,columns):
		pass
	
	def address_splitter(self,line,columns):
		pass
	
	def name_splitter(self,line,columns):
		pass
	
	def name_joiner(self,line,columns):
		pass
		
	def writer(self):
		path3 = "C:\Users/valued/Desktop/politech/politech csv/cleaned.csv"
		path4 = "C:\Users/valued/Desktop/politech/politech csv/junk.csv"
		with open(path3,"w+") as csvfile2:
			scribe = csv.writer(csvfile2,delimiter = '\n',lineterminator = '\n')
			scribe.writerows(cleaned)
		with open(path4,"w+") as csvfile3:
			scribe1 = csv.writer(csvfile3,delimiter = '\n',lineterminator = '\n')
			scribe1.writerows(junk)
		
	def scrubber(self):
		path1 = "C:\Users/valued/Desktop/politech/politech csv/*.csv"
		path2 = "C:\Users/valued/Desktop/politech/politech csv/*.xlsx"
		print path1,path2
		for files in glob.glob(path1):
			print files
			with open(files,"rb") as csvfile:
				sniffer = csv.reader(csvfile, delimiter = ',')
				headers = sniffer.next()
				for line in sniffer:
					print line
					if self.find_blanks(line) and self.find_incomplete(line) and self.state_abbreviations(line) and self.zip_scrub(line) == True:
						cleaned.append(line)
					else:
						junk.append(line)	
				
			
		for excel in glob.glob(path2):
					book =  xlrd.open_workbook(excel)
					sheet = book.sheets()
					sheet = book.sheet_by_index(0)
					for sheet in book.sheets():  
						for row in range(sheet.nrows):    
							if CSVcleaner.FindIncomplete(row) and CSVcleaner.state_abbreviations(row) and CSVcleaner.zip(row) == True:
								cleaned.append(row)
							else:
								junk.append(row)	
		self.writer()
		