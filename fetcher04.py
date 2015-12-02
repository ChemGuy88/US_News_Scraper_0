#!/user/bin/python

# Final version.
#
# Almost gave up on this one, but it gives 93 results for the 100 items
# processed. Regex sometimes works on IDLE interpreter
# but not when run as a function. For example, when ran on IDLE,
# University of Maryland gives 'Baltimore Hall, College Park, MD 20740, USA'
# but when run as a function it returns "Glenn L"

# This script tries to use the GoogleMaps API to fetch more specific 
# locations for universities. The problem is that it returns a bunch of
# different results, some without standard address (e.g., "Pittsburgh, 
# PA, USA" for Carnegie Mellon, without a street address).
# 
# Attempting using requests and getting info from HTML in browser.

import os
import re
import sys
import urllib
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBTR1wWZj9B70dBAOJTrMKlK256DsoBcTc')

n = '\n'

""" Address Fetcher

By Herman. Fetches address for universities.
"""

def main():
  print (n+'Welcome to the fetcher program',n)
#  file = sys.argv[1]
  file = r'C:\users\herman\gpe\usnews\rankscs-sorted.txt'
  university_list_file = os.path.abspath(file)
  mark = university_list_file.find('.txt')
  protofile = university_list_file[:mark]
  suffix = '-addresses.txt'
  tofile = protofile + suffix
  print ('Reading', university_list_file,n)
  university_list_data = open(university_list_file, 'r')
  print ('Turning to python list',n)  
  proto_university_list = university_list_data.read().split('\n')
  university_list = []
  for item in proto_university_list:
    university_list.append(item.split(';'))
  for value in university_list:
    if len(value) < 4:
      del university_list[university_list.index(value)]
  print ('Done. Closing file.',n)
  university_list_data.close()
  print ('Done. Printing list.',n)
  error_log_file_name = protofile + '-errors.txt'
  error_log_file = open(error_log_file_name, 'w')
  print ('Now searching for address via GoogleMaps API',n)
  newlist = []
  i = 1
  j = len(university_list)
  k = 0
  print(j,'items to work through',n)
  for list in university_list:
    try:
      print('Item',i,'of',j,n)
      location = '%s, %s' % (list[1], list[2])
      geocode_result = gmaps.geocode(location)
      re1 = '\'formatted_address\': \'([\w ,0-9\-]+)'
      formatted_address = re.search(re1,str(geocode_result))
      address = formatted_address.group(1)
      microlist = []
      for component in list:
        microlist.append(component)
      microlist.append(address)
      newlist.append(microlist)
    except Exception as e:
      error_log = 'Error for '+location+n+str(e)+2*n
      error_log_file.write(error_log)
      microlist = []
      for component in list:
        microlist.append(component)
      microlist.append(location)
      newlist.append(microlist)
      k += 1
      continue
    i += 1
  error_log_file.close()
  print ('There were',k,'errors.',n)
  writefile(tofile, newlist)
  
def writefile(tofile, newlist):
  export_file = open(tofile, 'w')
  print('Exporting new list to', tofile,n)
  for item in newlist:
    export_file.write(';'.join(item)+n)
  export_file.close()
  print('Done. Bye!')
  sys.exit(1)

if __name__ == '__main__':
  main()