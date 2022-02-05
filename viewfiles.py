# Put your code here
import os
def displayFiles(arg):
    if os.path.isfile(arg):
        print("File name:",arg,open(arg).read())
    else:
        print("Directory name:",arg)
        for file in os.listdir(arg):
            displayFiles(arg+"/"+file)


displayFiles("/root/sandbox/.testing")
