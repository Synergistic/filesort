import shutil, os, os.path

files_to_sort = os.listdir('new')
print files_to_sort
for file in files_to_sort:
	if '.txt' in file:
		if file[0].isalpha():
			shutil.copy('new\\'+ str(file), 'letters\\' + str(file))
		elif file[0].isdigit():
			shutil.copy('new\\'+ str(file), 'numbers\\' + str(file))