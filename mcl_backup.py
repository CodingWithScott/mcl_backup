## THIS FILE IS COPYRIGHTED
##  PRATT & WHITNEY 2017 
## FOR INTERNAL USE ONLY 
## MAY CONTAIN TECHNICAL DATA
#
# Author: Scott Felch
# Build date: 6/12/17
# Last updated: 6/6/26
#
# Note: If the location or name of files changes on the 
#       network, that will disrupt this script. File paths
#       are hard coded.
#
# TODO: Handle file not found exception
#       Show information and/or animation during transfer

# open input file -- READ mode
# open output file -- CREATE mode

# perform file transfer
# close files
# eject USB dick 

def copy(void):
	break

def main(void): 
	print('Transfer script initiating...')

	# Loop through list of read directories
	read_dir = '\\pusehf0r\hfb_mcl\grp\HFB_Mcl\\'
	write_dir = 'K:\MCL_BACKUP\Bond Quality'
	read_file = open(read_dir, 'r')
	write_file = open(write_dir, 'w+')



	


	read_dir.close()
	write_dir.close()
	read_file.close()
	write_file.close()


	break
