import os
import glob

class SortFiles:

    sourceFolder = '/home/[NAME]/Sites/sorting-files/media/from/'
    imageFolder = '/home/[NAME]/Sites/sorting-files/media/to/images/'
    videoFolder = '/home/[NAME]/Sites/sorting-files/media/to/videos/'
    musicFolder = '/home/[NAME]/Sites/sorting-files/media/to/music/'

    months = {
        "202001": 'January',
        "201902": 'February',
        "201903": 'March',
        "201904": 'April',
        "201905": 'May',
        "201906": 'June',
        "201907": 'July',
        "201908": 'August',
        "201909": 'September',
        "201910": 'October',
        "201911": 'November',
        "201912": 'December',
    };


    def organize(fileType, to):
        for types in fileType:
            files = glob.glob(SortFiles.sourceFolder + '**/*.' + types, recursive=True)
            for file in files:
                fileName = os.path.basename(file)
                path = to + fileName;
                if SortFiles.file_exist(path):
                    os.rename(file, to + fileName)
        
        # Organize Files into months
        SortFiles.organizeMonths(to)


    def file_exist(pathTest):
        #return true if file doesnt exist
        if os.path.isfile(pathTest) or os.path.isdir(pathTest) and pathTest is not '':
            return False
        return True

    def organizeMonths(to):
        SortFiles.createFolders(to)

        # Loop through months, and sort them into specific folders
        for key in SortFiles.months:
            files = glob.glob(to + '**' + key + '**', recursive=True)
            for file in files:
                fileName = os.path.basename(file)
                os.rename(to + fileName, to + '/' + SortFiles.months[key] + '/' + fileName)

    def createFolders(to):
        for key in SortFiles.months:
            try:
                os.mkdir(to + SortFiles.months[key])
            except OSError:
                print ("Creation of the directory %s failed.")

        
                    

# Sort images, videos, and music
# after thats done,
SortFiles.organize(['jpg', 'jpeg', 'png', 'gif'], SortFiles.imageFolder)
SortFiles.organize(['mp4'], SortFiles.videoFolder)
SortFiles.organize(['mp3', 'wav'], SortFiles.musicFolder)