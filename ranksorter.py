#!/usr/bin/python

import os
import re
import sys
import urllib

n = '\n'

"""US News Rank Sorter
"""

def MyKey(s):
  return s[1]

def main():
  file = sys.argv[1]
  print ('the file you are analyzing is\'', file, '\'.', n)
  # creation of destination file
  abspath = os.path.abspath(file)
  mark = abspath.find('.txt')
  protofile = abspath[:mark]
  suffix = '-sorted.txt'
  tofile = protofile + suffix
  print ('you are exporting to\'', tofile, '\'', n)
  print ('opening file', n)
  fileobject = open(file, 'r')
  print ('reading file', n)
  filetext = fileobject.read()
#  print (filetext, n)
  tuples_list = []
  re1 = '#(\d\d?)\n*'
  re2 = '(Tie\n)?'
  re3 = '([A-Za-z\- &.,()]+)\n*'
  re4 = '([A-Za-z\- .]+, [A-Z\-]+)\n*'
  re5 = '(\d\.\d)'
  tuples_list = re.findall(re1+re3+re4+re5, filetext)
  print ('there were', len(tuples_list), 'schools found.', n)
  print ('exporting file to', tofile, n)
  export_file = open(tofile, 'w')
  for item in tuples_list:
    export_file.write(';'.join(item) + '\n')
    


  
  sys.exit(1)

if __name__ == '__main__':
  main()
