import shutil, os, os.path

'''Look at all files in a target directory and then
sorts them into appropriate folders. It looks for a
file with a name that is either a letter or number.'''

#create a list of the items in my target directory \new\
files_to_sort = os.listdir('new')

#iterate through the items in the list from \new\
for file in files_to_sort:

	#pull out the files I want, ignored the folders, in this case .txt files
	if '.txt' in file:
	
		#if its a letter...
		if file[0].isalpha():
		
			#copy it to the letters directory with the same name
			shutil.copy('new\\'+ str(file), 'letters\\' + str(file))
			
		#otherwise if its a number...
		elif file[0].isdigit():
		
			#copy it to the numbers directory with the same name
			shutil.copy('new\\'+ str(file), 'numbers\\' + str(file))