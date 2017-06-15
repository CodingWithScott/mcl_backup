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
#       Eject USB dick -- is this possible from Python? 
#		       			w/o admin access? maybe bad idea.


# Hardcoded file paths that are super ugly
bond_log_src = 'Z:\\Hfb\\MCL LAB HFB\\Bond Log Sheets'
bond_quality_src = 'Z:\\Hfb\\MCL LAB HFB\\HFB_Bond_Quality'
wl_src = 'Z:\\Hfb\\MCL LAB HFB\\MCL Working List 2016 - Active.xlsx'

bond_log_dest = 'G:\\MCL Back-up\\Bond LOG Sheets'
bond_quality_dest = 'G:\\MCL Back-up\HFB_Bond_Quality'
wl_dest = 'G:\\MCL Back-up\\Working list\\'

import errno 	# Exception handling
import shutil	# File handling module

def copy_file(src, dest):
	try:
		shutil.copy(src, dest)
	# eg. src and dest are the same file
	except shutil.Error as e:
		print('Error: %s' % e)
	# eg. source or destination doesn't exist
	except IOError as e:
		print('Error: %s' % e.strerror)

def copy_anything(src, dst):
	try:
		shutil.copytree(src, dst)
	except OSError as exc: # python >2.5
		if exc.errno == errno.ENOTDIR:
			shutil.copy(src, dst)
		else: raise

# Receives path to file OR folder of files
def create_temp(dest):
	shutil.mov(dest, dest + '.TMP')
	print('Marked temp:\t%s')

def clear_temp():
	# https://automatetheboringstuff.com/chapter9/
	for filename in os.listdir():
		if filename.endswith('.TMP'):
			#os.unlink(filename)
			print('Deleted (air quotes):\t%s', filename)


def main(): 
	print('Transfer initiating...')
	# TODO: Day of week logic
	src_paths = [bond_log_src, bond_quality_src, wl_src]
	dest_paths = [bond_log_dest, bond_quality_dest, wl_dest]

	for curr_path in range(2):
		create_temp(curr_path) ## STILL BROKEN
		copy_anything(src_paths[curr_path], dest_paths[curr_path])
		clear_temp()		
	
	print('Done!')


if __name__ == "__main__":
	main()