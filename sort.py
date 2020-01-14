import os
import glob

#image filetypes

def organize(file_types, to):
	for types in file_types:
		files = glob.glob('E:/Users/Samsung S6/FTP3/**/*.' + types, recursive=True)
		for file in files:
			filename = os.path.basename(file)
			path = to + filename;
			if file_exist(path):
					os.rename(file, to + filename)



def file_exist(pathtest):
	#return true if file doesnt exist
	if os.path.isfile(pathtest) or os.path.isdir(pathtest) and pathtest is not '':
		return False
	else:
		return True


organize(['jpg', 'jpeg', 'png', 'gif'], 'E:/Users/Samsung S6/Media/sorted/images/')
organize(['mp4'], 'E:/Users/Samsung S6/Media/sorted/videos/')
organize(['mp3', 'wav'], 'E:/Users/Samsung S6/Media/sorted/music/')