# This class will load a resume in a doc file or pdf and convert the contents
# to a text document and return it
import os.path
import re
import errno
import sys

def load_resume(resume_file_path):

    try:
        file = open(resume_file_path, 'r')
        file.close()
    
    except IOError as e:
        if e.errno == errno.EACCES:
            print("file exists, but isn't readable")
        elif e.errno == errno.ENOENT:
            print("files isn't readable because it isn't there")
    #TODO
    # Need to use pdfminer or some other tool to take the file and convert it
    return(file)



if __name__ == "__main__":
    load_resume(sys.argv[1])


