#!/usr/bin/python
# fh = open('/tmp/file.txt')

try:
    fh = open('/home/rahul/testfile.txt')
    # if fh.name is not '/home/rahul/testfile.txt':
    if fh.name is  '/home/rahul/testfile.txt':
        raise NameError("raising manual exception")
        # raise Exception("raising manual exception")
    # var = var_bad


except IOError as Err:
    print 'IOError: ', Err

except NameError as Err:
    print 'NameError: ', Err

except Exception as e:
    print 'Soory ! Something went wrong: {}'.format(e)

# except CustomException as e:
#     print "Error raised: {}".format(e)

else: #No except run
    print fh.read()
    print "Closing file: {}".format(fh.name)
    fh.close()

finally: #Always runs

    print 'I am done with Execution'




# print('Converting')
# print(int('1'))
# print('Done')


# print('Converting')
# try:
#     print(int('x'))
# except ValueError as Err:
#     print('Conversion Failed')
#     print "Error: ", Err
# else: #If no-except
#     print('Conversion successful')
# finally:
#     print('Done')

# print('Converting')
# try:
#      print(int('x'))
# finally: #Always
#     print('Done')