#!/usr/bin/python
#Function: clear the tags for the xml/html file.
import sys
import os
import string
import re

if len(sys.argv) < 3 or (not os.path.isfile(sys.argv[1])):
    print "Usage: clear-tag.py target result"
    print "       target: the xml/html file that you will deal with, this file must exist"
    print "       result: the file that will save the result"
    sys.exit()

target_file_name = sys.argv[1]
result_file_name = sys.argv[2]

if not os.path.isfile(result_file_name):
    os.system("touch " + result_file_name)

target_file = open(target_file_name, 'r')
content = target_file.read()
content = re.sub(r' +', ' ', re.sub(r'(<)([^<>]+)(>)', ' ', content ))
content = content.strip()

result_file = open(result_file_name, 'w')
result_file.write(content)
target_file.close()
result_file.close()

