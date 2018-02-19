#!/usr/bin/python
import sys, getopt

'''
print "Total Number of arguments: ",len(sys.argv)
print "Arguments list : ",sys.argv

count = 1
for arg in sys.argv:
    print "Argument is ", arg
'''


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
    if (len(sys.argv) == 1):
        list = ['-h']
        main (list)
    else:
        main(sys.argv[1:])
