## THIS FILE IS COPYRIGHTED
##  PRATT & WHITNEY 2017 
## FOR INTERNAL USE ONLY 
## MAY CONTAIN TECHNICAL DATA
#
# Author: Scott Felch
# Build date: 6/12/17
# Last updated: 6/13/26
#
# Note: If the location or name of files changes on the 
#       network, that will disrupt this script. File paths
#       are hard coded.
#
# TODO: Handle file not found exception
#       Show information and/or animation during transfer

# perform file transfer
# close files
# eject USB dick -- is this possible from Python? 
#					w/o admin access? maybe bad idea.

import shutil

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)

def main(): 
	print('Transfer initiating...')

	wl_src = 'T:\\Music\\13. Track13.wav'
	wl_dest = 'c:\\Users\\sfelc\\Desktop\\Track 13 BACKUP.wav'

	copy_file(wl_src, wl_dest)
		
	print('Done!')

	


	# break

if __name__ == "__main__":
	main()

