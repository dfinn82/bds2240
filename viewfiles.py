#recursive function to list files in a directory
import os
def displayFiles(arg):
    #if a file, print file name and path
    if os.path.isfile(arg):
        print("File name:",arg,open(arg).read())
    #else we have a directory, print directory and then run function on that dir
    else:
        print("Directory name:",arg)
        for file in os.listdir(arg):
            displayFiles(arg+"/"+file)


displayFiles("/root/sandbox/.testing")
