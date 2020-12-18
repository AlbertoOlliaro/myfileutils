import getopt
import sys
from os import listdir
from os.path import isfile, join
from PyPDF2 import PdfFileMerger


def main(argv):
    inputfiles = []
    outputfile = ''
    inputdir = None
    try:
        opts, args = getopt.getopt(argv, "hi:o:d:", ["ifile=", "idir=", "ofile="])
    except getopt.GetoptError:
        print('mergepdfs.py -i <inputfile> [-i<inputfile>] -d <inputdirectory> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage:\n'
                  'mergepdfs.py -i <inputfile> [-i<inputfile>] -o <outputfile> \n'
                  'or mergepdfs.py -d <inputdirectory> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfiles.append(arg)
        elif opt in ("-d", "--idir"):
            inputdir = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print('Input files are ', str(inputfiles))
    print('Input dir is ', inputdir)
    print('Output file is ', outputfile)

    if inputdir:
        files_list = [join(inputdir, f) for f in listdir(inputdir) if isfile(join(inputdir, f)) and f.endswith('.pdf')]
    else:
        files_list = inputfiles

    print(str(files_list))

    merger = PdfFileMerger()
    for pdf in files_list:
        print("file: " + str(pdf))
        merger.append(pdf)

    merger.write(outputfile)
    merger.close()


if __name__ == '__main__':
    main(sys.argv[1:])
