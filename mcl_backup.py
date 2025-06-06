# THIS FILE IS COPYRIGHTED
# PRATT & WHITNEY 2017
# FOR INTERNAL USE ONLY
# MAY CONTAIN TECHNICAL DATA
#
# Author: Scott Felch
# Build date: 7/31/17
#
# Note: If the location or name of files changes on the
#       network, that will disrupt this script. File paths
#       are hard coded.

import datetime  # Day of week checking
import hashlib   # SHA1 / MD5 hashing
import os        # File handling
import shutil    # File copying


# Hardcoded file paths
BOND_LOG_SRC_1 = 'G:\\Hfb\\MCL LAB HFB\\Bond Log Sheets\\Bond log 1.xlsx'
BOND_LOG_SRC_2 = 'G:\\Hfb\\MCL LAB HFB\\Bond Log Sheets\\Bond log 2.xlsx'
BOND_LOG_SRC_3 = 'G:\\Hfb\\MCL LAB HFB\\Bond Log Sheets\\Bond log 3.xlsx'

BOND_QUAL_SRC_1 = 'G:\\Hfb\\MCL LAB HFB\\HFB_Bond_Quality\\Bond quality 1.xlsx'
BOND_QUAL_SRC_2 = 'G:\\Hfb\\MCL LAB HFB\\HFB_Bond_Quality\\Bond quality 2.xlsx'
BOND_QUAL_SRC_3 = 'G:\\Hfb\\MCL LAB HFB\\HFB_Bond_Quality\\Bond quality 3.xlsx'

BOND_LOG_DEST_1 = 'Z:\\MCL Back-up\\Bond LOG Sheets\\Bond log 1.xlsx'
BOND_LOG_DEST_2 = 'Z:\\MCL Back-up\\Bond LOG Sheets\\Bond log 2.xlsx'
BOND_LOG_DEST_3 = 'Z:\\MCL Back-up\\Bond LOG Sheets\\Bond log 3.xlsx'

BOND_QUAL_DEST_1 = 'Z:\\MCL Back-up\\HFB_Bond_Quality\\Bond quality 1.xlsx'
BOND_QUAL_DEST_2 = 'Z:\\MCL Back-up\\HFB_Bond_Quality\\Bond quality 2.xlsx'
BOND_QUAL_DEST_3 = 'Z:\\MCL Back-up\\HFB_Bond_Quality\\Bond quality 3.xlsx'

WL_SRC = 'G:\\Hfb\\MCL LAB HFB\\MCL Working List 2016 - Active.xlsx'
WL_DEST = 'Z:\\MCL Back-up\\Working list\\'


# Copy file from 'src' absolute path to 'dest' absolute path
def copy(src, dest):
    if (os.path.isfile(src)):
        shutil.copy(src, dest)


# Backup thumbdrive before transferring from network.
# Receives absolute path to file
def create_temp(file_path):
    # Verify valid path
    if not (os.path.exists(file_path)):
        print(' \'{}\' not found, no temp file created.'.format(file_path))
        return

    os.rename(file_path, file_path + '.TMP')


def del_temp(file_path):
    file_dir = file_path
    while (file_dir[-1] != '\\'):
        file_dir = file_dir[:len(file_dir) - 1]

    rm_temp = file_path + '.TMP'
    os.unlink(rm_temp)


def verify_data(src, dest):
    filename = src.split('\\')[-1]

    src_md5_hasher = hashlib.md5()
    src_sha1_hasher = hashlib.sha1()

    dest_md5_hasher = hashlib.md5()
    dest_sha1_hasher = hashlib.sha1()

    with open(src, 'rb') as md5_file:
        buf = md5_file.read()
        src_md5_hasher.update(buf)

    with open(src, 'rb') as sha1_file:
        buf = sha1_file.read()
        src_sha1_hasher.update(buf)

    with open(dest, 'rb') as md5_file:
        buf = md5_file.read()
        dest_md5_hasher.update(buf)

    with open(dest, 'rb') as sha1_file:
        buf = sha1_file.read()
        dest_sha1_hasher.update(buf)

    print('\t\'{}\' integrity check:'.format(filename))

    if (src_md5_hasher.hexdigest() == dest_md5_hasher.hexdigest()):
        print('md5:\t{}\t\t\t[OK]'.format(src_md5_hasher.hexdigest()))
    else:
        print('\t\tmd5 mismatch:\t', filename)
        print('\tsource:\t', src_md5_hasher.hexdigest())
        print('\tdest:\t', dest_md5_hasher.hexdigest())
        print('\t\tMD5 check:\tfailed!')
        return False
    if (src_sha1_hasher.hexdigest() == dest_sha1_hasher.hexdigest()):
        print('sha1:\t{}\t\t[OK]'.format(src_sha1_hasher.hexdigest()))
    else:
        print('\t\tsha1 mismatch:\t', filename)
        print('source:\t', src_sha1_hasher.hexdigest())
        print('dest:\t', dest_sha1_hasher.hexdigest())
        print('SHA1 check:\tfailed!')
        return False

    return True


# Restore thumbdrive to original state if file transfer fails, trimp .TMP off
# of filenames.
def uncreate_temp(path):
    # Verify valid path
    if not (os.path.exists(path)):
        print('uncreate_temp() error: path \'{}\' not found!'.format(path))
        return

    trim_path = path
    while(trim_path[:-4] == '.TMP'):
        os.rename(trim_path, trim_path[:-4])
        trim_path = trim_path[:-4]


def main():
    # Create mutable string from constant
    wl_dest = WL_DEST

    if (datetime.datetime.today().weekday() == 0):
        wl_dest = wl_dest + '1 Monday\\MCL Working List 2016 - Active.xlsx'
    elif (datetime.datetime.today().weekday() == 1):
        wl_dest = wl_dest + '2 Tuesday\\MCL Working List 2016 - Active.xlsx'
    elif (datetime.datetime.today().weekday() == 2):
        wl_dest = wl_dest + '3 Wednesday\\MCL Working List 2016 - Active.xlsx'
    elif (datetime.datetime.today().weekday() == 3):
        wl_dest = wl_dest + '4 Thursday\\MCL Working List 2016 - Active.xlsx'
    elif (datetime.datetime.today().weekday() == 4):
        wl_dest = wl_dest + '5 Friday\\MCL Working List 2016 - Active.xlsx'
    else:
        wl_dest = wl_dest + '6 Weekend\\MCL Working List 2016 - Active.xlsx'

    src_files = [BOND_LOG_SRC_1, BOND_LOG_SRC_2, BOND_LOG_SRC_3,
                 BOND_QUAL_SRC_1, BOND_QUAL_SRC_2, BOND_QUAL_SRC_3,
                 WL_SRC]
    dest_files = [BOND_LOG_DEST_1, BOND_LOG_DEST_2, BOND_LOG_DEST_3,
                  BOND_QUAL_DEST_1, BOND_QUAL_DEST_2, BOND_QUAL_DEST_3,
                  wl_dest]

    print('======================================================')
    print('==              Transfer initiating...              ==')
    print('======================================================')
    print()
    for curr_file in range(len(src_files)):
        create_temp(dest_files[curr_file])
        copy(src_files[curr_file], dest_files[curr_file])
        if (verify_data(src_files[curr_file], dest_files[curr_file])):
            del_temp(dest_files[curr_file])
        else:
            print('======================================================')
            print('==       Failed! thumb drive files unchanged.       ==')
            print('======================================================')
            uncreate_temp(dest_files[curr_file])

    print()
    print('======================================================')
    print('==                     Success!                     ==')
    print('======================================================')
    print()
    os.system('pause')  # 'press any key to continue'


if __name__ == "__main__":
    main()
