import getopt
import sys
from os import listdir
from os import rename
from os.path import isfile, join


def main(argv):
    inputfiles = []
    inputdir = None
    try:
        opts, args = getopt.getopt(argv, "hi:o:d:", ["ifile=", "idir=", "ofile="])
    except getopt.GetoptError:
        print('month2num.py -i <inputfile> [-i<inputfile>] -d <inputdirectory> ')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage:\n'
                  'this script needs to be run within the directory\n'
                  'month2num.py -i <inputfile> [-i<inputfile>] \n'
                  'or month2num.py -d <inputdirectory> ')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfiles.append(arg)
        elif opt in ("-d", "--idir"):
            inputdir = arg

    print('Input files are ', str(inputfiles))
    print('Input dir is ', inputdir)

    if inputdir:
        files_list = [join(inputdir, f) for f in listdir(inputdir) if isfile(join(inputdir, f)) and f.endswith('.pdf')]
    else:
        files_list = inputfiles

    print(str(files_list))

    for pdf in files_list:
        new_filename = replace_month_with_number(str(pdf))
        if str(pdf) != new_filename:
            print("file: " + str(pdf))
            print("renamed to: " + new_filename)
            rename(str(pdf), new_filename)


def replace_month_with_number(string):
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']

    for i in range(len(month_list)):
        string = string.replace(month_list[i], str(i+1).zfill(2))
    return string
    # string = string.replace('January', '01')
    # string = string.replace('February', '02')
    # string = string.replace('March', '03')
    # string = string.replace('April', '04')
    # string = string.replace('May', '05')
    # string = string.replace('June', '06')
    # string = string.replace('July', '07')
    # string = string.replace('August', '08')
    # string = string.replace('September', '09')
    # string = string.replace('October', '10')
    # string = string.replace('November', '11')
    # return string.replace('December', '12')


if __name__ == '__main__':
    main(sys.argv[1:])
