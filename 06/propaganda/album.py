import re
import sys
import logging

logging.basicConfig(filename='albums.txt', level=logging.DEBUG)

logging.debug([line for line in open(sys.argv[1], "r")
               if re.search(sys.argv[2], line)])
