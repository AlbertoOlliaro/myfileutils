from PIL import Image
import getopt
import sys


def main(argv):
    inputfile = ''
    outputfile = ''

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('image2pdf.py -i <inputimagefile>  -o <outputfile.pdf>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage:'
                  '\nimage2pdf.py -i <inputimagefile> -o <outputfile.pdf>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print('Input file is ', str(inputfile))
    print('Output file is ', outputfile)

    image = Image.open(inputfile, mode='r')
    im = image.convert('RGB')
    im.save(outputfile)


if __name__ == '__main__':
    main(sys.argv[1:])
