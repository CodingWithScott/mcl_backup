import datetime  # Day of week checking
import os        # File handling

BOND_LOG_DEST = 'Z:\\MCL Back-up\\Bond LOG Sheets\\'
BOND_QUAL_DEST = 'Z:\\MCL Back-up\\HFB_Bond_Quality\\'
WL_DEST = 'Z:\\MCL Back-up\\Working list\\'


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
        print('Unmarked temp:\t{}', path)
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

    dest_paths = [BOND_LOG_DEST, BOND_QUAL_DEST, wl_dest]

    print('Reverting TMP...\n')
    for curr_path in range(2):
        print('uncreate_temp(\'{}\'):\n'.format(dest_paths[curr_path]))
        uncreate_temp(dest_paths[curr_path])


if __name__ == "__main__":
    main()
