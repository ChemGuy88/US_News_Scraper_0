#!/user/bin/python
# Info from https://automatetheboringstuff.com/chapter11/
# Abandoned
# This tries to get address information by going to Googel maps via a
# browser. However, this cannot get the address from the browser and
# add it to the list. Next attempt tries that via requests module

import os
import re
import sys
import urllib
import googlemaps
import webbrowser

n = '\n'

""" Address Fetcher

By Herman. Fetches address for universities.
"""

def main():
  print (n+'welcome to the fetcher program',n)
  file = sys.argv[1]
  university_list_file = os.path.abspath(file)
  mark = university_list_file.find('.txt')
  protofile = university_list_file[:mark]
  suffix = '-addresses.txt'
  tofile = protofile + suffix
  print ('reading', university_list_file,n)
  university_list_data = open(university_list_file, 'r')
  print ('turning to python list',n)  
  proto_university_list = university_list_data.read().split('\n')
  university_list = []
  for item in proto_university_list:
    university_list.append(item.split(';'))
#  print(n,university_list,n)
  print ('done',n)
  university_list_data.close()
  print ('done. Printing list.',n)
  for line in university_list:
    print(line)
  print ('concatenating with address via webscraping',n)
# mapIt.py
  newlist = []
  i = 1
  j = len(university_list)
  print(j,'items to work through',n)
  for line in university_list:
    if i == 5:
      sys.exit(1)
    try:
      print('item',i,'of',j,n)
      location = '%s, %s' % (line[1], line[2])
      print(' ',location,n)
      webbrowser.open('https://www.google.com/maps/place/'+location)
      print('  found address:',address,n)
      new_line = line+address
      print('  concatenating line with address:',new_line,n)
      newlist.extend(line+address)
    except Exception as e:
      print('  Encountered error:',n,e,n,n)
    i += 1
  export_file = open(tofile, 'w')
  print('exporting new list to',export_file)
  for item in newlist:
    export_file.write(';'.join(item)+n)
  print('bye!')
  sys.exit(1)

if __name__ == '__main__':
  main()