import sys
from fsplit.filesplit import Filesplit

fs = Filesplit()

#Callback function to print the split outputs in the terminal 
def split_cb(f, s):
    print("file: {0}, size: {1}".format(f, s))

#file -> input file name
#split_size -> size of every splits in bytes
#output_dir -> target directory to store the splits.
fs.split(file=sys.argv[1], split_size=1000000, output_dir="/home/anamika/Assignment/Splits", callback=split_cb)
