# THIS FILE IS COPYRIGHTED
# PRATT & WHITNEY 2017
# FOR INTERNAL USE ONLY
# MAY CONTAIN TECHNICAL DATA
#
# Author: Scott Felch
# Build date: 6/12/17
# Last updated: 6/13/26
#
# Note: If the location or name of files changes on the
#       network, that will disrupt this script. File paths
#       are hard coded.
#
# TODO: Show information and/or animation during transfer
#       Make it so fault-tolerant that Camila could use it

import errno    # Exception handling
import os       # File handling
import shutil   # File handling module


# Hardcoded file paths
bond_log_src = 'Z:\\Hfb\\MCL LAB HFB\\Bond Log Sheets'
bond_quality_src = 'Z:\\Hfb\\MCL LAB HFB\\HFB_Bond_Quality'
wl_src = 'Z:\\Hfb\\MCL LAB HFB\\MCL Working List 2016 - Active.xlsx'

bond_log_dest = 'G:\\MCL Back-up\\Bond LOG Sheets'
bond_quality_dest = 'G:\\MCL Back-up\HFB_Bond_Quality'
wl_dest = 'G:\\MCL Back-up\\Working list\\'


# Totally depcrecated?
# def copy_file(src, dest):
#     try:
#         shutil.copy(src, dest)
#     # eg. src and dest are the same file
#     except shutil.Error as e:
#         print('Error: %s' % e)
#     # eg. source or destination doesn't exist
#     except IOError as e:
#         print('Error: %s' % e.strerror)


# Copy folder OR file
def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as exc:  # python >2.5
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            raise


# Receives path to file OR folder of files
def create_temp(path):
    path_is_file = False if (path[-1] == '\\') else True

    # Verify valid path
    if not (os.path.exists(path)):
        print('Error: path \'%s\' not found!', path)
        return

    if (path_is_file):
        os.rename(path, path + '.TMP')
        print('Marked temp:\t%s', path)
    else:
        files = os.listdir(path)
        print('files:')
        print(files)
        for file in files:
            os.rename(os.path.join(path, file),
                      os.path.join(path, file + '.TMP'))


# TODO: need to get this to accept a path, not default working directory
def clear_temp():
    # https://automatetheboringstuff.com/chapter9/
    for filename in os.listdir():
        if filename.endswith('.TMP'):
            # os.unlink(filename)
            print('Deleted (air quotes):\t%s', filename)


# TODO: Implement this
def verify_data():
    print('Data looks good! (jk, didn\'t check yet')


# TODO: Implement this
def progress_bar():
    print('[            0%           ]')
    print('[==         10%           ]')
    print('[====       20%           ]')
    print('[======     30%           ]')
    print('[========   40%           ]')
    print('[========== 50%           ]')
    print('[========== 60% ==        ]')
    print('[========== 70% ====      ]')
    print('[========== 80% ======    ]')
    print('[========== 90% ========  ]')
    print('[========= 100% ==========]')


def main():
    print('Transfer initiating...')
    # TODO: Day of week logic
    src_paths = [bond_log_src, bond_quality_src, wl_src]
    dest_paths = [bond_log_dest, bond_quality_dest, wl_dest]

    for curr_path in range(2):
        create_temp(curr_path)
        copy(src_paths[curr_path], dest_paths[curr_path])
        verify_data()
        clear_temp()

    print('Done!')


if __name__ == "__main__":
    main()
