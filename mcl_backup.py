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


import datetime  # Day of week checking
import hashlib   # SHA1 / MD5 hashing
import os        # File handling
import shutil    # File handling module


# Hardcoded file paths
BOND_LOG_SRC = 'G:\\Hfb\\MCL LAB HFB\\Bond Log Sheets\\'
BOND_QUAL_SRC = 'G:\\Hfb\\MCL LAB HFB\\HFB_Bond_Quality\\'
WL_SRC = 'G:\\Hfb\\MCL LAB HFB\\MCL Working List 2016 - Active.xlsx'

BOND_LOG_DEST = 'Z:\\MCL Back-up\\Bond LOG Sheets\\'
BOND_QUAL_DEST = 'Z:\\MCL Back-up\\HFB_Bond_Quality\\'
WL_DEST = 'Z:\\MCL Back-up\\Working list\\'


# Copy folder (Does it support file?)
def copy(src, dest):
    print('copy(\'{0}\' , \'{1}\')\n'.format(src, dest))

    src_files = os.listdir(src)

    for src_file_name in src_files:
        src_full_path = os.path.join(src, src_file_name)
        dest_full_path = os.path.join(dest, src_file_name)
        if (os.path.isfile(src_full_path)):
            shutil.copy(src_full_path, dest_full_path)


# Backup thumbdrive before transferring from network.
# Receives path to file OR folder of files.
def create_temp(path):
    path_is_file = False if (path[-1] == '\\') else True

    # Verify valid path
    if not (os.path.exists(path)):
        print(' \'{}\' not found, no temp file created.'.format(path))
        return

    if (path_is_file):
        os.rename(path, path + '.TMP')
        print('Marked temp:\t', path)
    else:
        files = os.listdir(path)
        print('files before appending TMP:')
        print(files)
        print('\n')
        for file in files:
            os.rename(os.path.join(path, file),
                      os.path.join(path, file + '.TMP'))
        files = os.listdir(path)
        print('files after appending TMP:')
        print(files)
        print('\n')


def del_temp(path):
    print('cwd:\t', os.getcwd())
    # https://automatetheboringstuff.com/chapter9/
    for filename in os.listdir(path):
        if filename.endswith('.TMP'):
            full_path = path + filename
            os.unlink(full_path)
            print('Deleted:\t', full_path)


def verify_data(src, dest):
    path_is_file = False if (path[-1] == '\\') else True

    src_md5_hasher = hashlib.md5()
    src_sha1_hasher = hashlib.sha1()

    dest_md5_hasher = hashlib.md5()
    dest_sha1_hasher = hashlib.sha1()

    if (path_is_file):
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

        print(src, ' integrity check...')
        print('md5:\t', src_md5_hasher.hexdigest())
        print('sha1:\t', src_sha1_hasher.hexdigest())

        print(dest, ' integrity check...')
        print('md5:\t', dest_md5_hasher.hexdigest())
        print('sha1:\t', dest_sha1_hasher.hexdigest())

        if (src_md5_hasher.hexdigest() == dest_md5_hasher.hexdigest()):
            print('MD5 check:\tok!')
        else:
            print('MD5 check:\tfailed!')
            return False
        if (src_sha1_hasher.hexdigest() == dest_sha1_hasher.hexdigest()):
            print('SHA1 check:\tok!')
        else:
            print('SHA1 check:\tfailed!')
            return False
    else:
        src_files = os.listdir(src)
        dest_files = os.listdir(dest)

        for curr_file in range(len(dest_files)):
            src_md5_hasher = hashlib.md5()
            src_sha1_hasher = hashlib.sha1()

            dest_md5_hasher = hashlib.md5()
            dest_sha1_hasher = hashlib.sha1()

            with open(src_files[curr_file], 'rb') as md5_file:
                buf = md5_file.read()
                src_md5_hasher.update(buf)

            with open(src_files[curr_file], 'rb') as sha1_file:
                buf = sha1_file.read()
                src_sha1_hasher.update(buf)

            with open(dest_files[curr_file], 'rb') as md5_file:
                buf = md5_file.read()
                dest_md5_hasher.update(buf)

            with open(dest_files[curr_file], 'rb') as sha1_file:
                buf = sha1_file.read()
                dest_sha1_hasher.update(buf)

            print(src_files[curr_file], ' integrity check...')
            print('md5:\t', src_md5_hasher.hexdigest())
            print('sha1:\t', src_sha1_hasher.hexdigest())

            print(dest_files[curr_file], ' integrity check...')
            print('md5:\t', dest_md5_hasher.hexdigest())
            print('sha1:\t', dest_sha1_hasher.hexdigest())

            if (src_md5_hasher.hexdigest() == dest_md5_hasher.hexdigest()):
                print('MD5 check:\tok!')
            else:
                print('MD5 check:\tfailed!')
                return False
            if (src_sha1_hasher.hexdigest() == dest_sha1_hasher.hexdigest()):
                print('SHA1 check:\tok!')
            else:
                print('SHA1 check:\tfailed!')
                return False

    return True


# Restore thumbdrive to original state if file transfer fails.
def uncreate_temp(path):
    path_is_file = False if (path[-1] == '\\') else True

    # Verify valid path
    if not (os.path.exists(path)):
        print('Error: path \'{}\' not found!'.format(path))
        return

    # Trim .TMP off of filenames
    if (path_is_file):
        while(path[:-4] == '.TMP'):
            os.rename(path, path[:-4])
        print('Unmarked temp:\t{0}', path)
    else:
        # path == directory, file == file w/in directory
        files = os.listdir(path)
        for orig_file in files:
            trim_file = orig_file

            while(trim_file[-4:] == '.TMP'):
                os.rename(os.path.join(path, trim_file),
                          os.path.join(path, trim_file[:-4]))
                trim_file = trim_file[:-4]


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

    src_paths = [BOND_LOG_SRC, BOND_QUAL_SRC, WL_SRC]
    dest_paths = [BOND_LOG_DEST, BOND_QUAL_DEST, wl_dest]

    print('Transfer initiating...')
    for curr_path in range(3):
        create_temp(dest_paths[curr_path])
        copy(src_paths[curr_path], dest_paths[curr_path])
        if (verify_data(src_paths[curr_path], dest_paths[curr_path])):
            del_temp(dest_paths[curr_path])
            print('\n%s transferred successfully.' % dest_paths[curr_path])
        else:
            print('\n%s transferred failed!' % dest_paths[curr_path])
            print('Transfer aborted, thumb drive files unchanged.')
            uncreate_temp(dest_paths[curr_path])

    os.system('pause')  # 'press any key to continue'


if __name__ == "__main__":
    main()
