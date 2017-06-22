import os       # File handling
import shutil   # File handling module


def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
    # eg. src and dest are the same file
    except shutil.Error as e:
        print('Error: %s' % e)
    # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: %s' % e.strerror)


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
            # copy_file(file, file + '.TMP)')
            os.rename(os.path.join(path, file),
                      os.path.join(path, file + '.TMP'))


def uncreate_temp(path):
    path_is_file = False if (path[-1] == '\\') else True

    # Verify valid path
    if not (os.path.exists(path)):
        print('Error: path \'%s\' not found!', path)
        return

    # Trim .TMP off of filenames
    if (path_is_file):
        os.rename(path, path[:-4])
        print('Marked temp:\t%s', path)
    else:
        files = os.listdir(path)
        print('files:')
        print(files)
        for file in files:
            # copy_file(file, file[:-4])
            os.rename(os.path.join(path, file),
                      os.path.join(path, file[:-4]))


# TODO: need to get this to accept a path, not default working directory
def clear_temp(path):
    print('cwd:\t%s', os.currdir())
    # https://automatetheboringstuff.com/chapter9/
    for filename in os.listdir(path):
        if filename.endswith('.TMP'):
            # os.unlink(filename)
            print('Deleted (air quotes):\t%s', filename)


def main():
    path = 'C:\\Users\\sfelc\\Desktop\\lots_of_files_BACKUP\\'
    # path = 'C:\\Users\\sfelc\\Desktop\\monkey.jpg'

    # create_temp(path)
    uncreate_temp(path)
    # clear_temp(path)


if __name__ == "__main__":
    main()
