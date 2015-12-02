#!/user/bin/python

# v05, latest using Google Maps scrapes with BS
#
# Stuck b/c address is embedded in JS.
#
# v04 works reasonably well. About 93 of the 100 items searched return
# a value, most of them are good. However, I want a more accurate result
# from Google Maps. So this version will try to scrape addresses from
# a browser Google Maps search.

import os
import re
import sys
import urllib
import urllib.request
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup

br = RoboBrowser(user_agent='a python robot')

n = '\n'

""" Address Fetcher

By Herman. Fetches address for universities.
"""

def FetchAddress(University_list):
  1+1

def main():
  print (n+'Welcome to the fetcher program',n)
#  file = sys.argv[1]
  file = r'C:\users\herman\gpe\usnews\rankscs-sorted.txt'
  university_list_file = os.path.abspath(file)
  mark = university_list_file.find('.txt')
  protofile = university_list_file[:mark]
  suffix = '-addresses.txt'
  tofile = protofile + suffix
#  print ('Reading', university_list_file,n)
  university_list_data = open(university_list_file, 'r')
#  print ('Turning to python list',n)  
  proto_university_list = university_list_data.read().split('\n')
  university_list = []
  for item in proto_university_list:
    university_list.append(item.split(';'))
  for value in university_list:
    if len(value) < 4:
      del university_list[university_list.index(value)]
#  print ('Done. Closing file.',n)
  university_list_data.close()
#  print ('Done. Printing list.',n)
  error_log_file_name = protofile + '-errors.txt'
  error_log_file = open(error_log_file_name, 'w')
#  print ('Now searching for address via GoogleMaps API',n)
  newlist = []
  i = 1
  j = len(university_list)
  k = 0
  print(j,'items to work through',n)
  for list in university_list:
    if i == 3:
      sys.exit(1)
    try:
      print('Item',i,'of',j,n)
      location = '%s, %s' % (list[1], list[2])
      
      location_dig = location.replace(' ', '+')
      url = r'https://www.google.com/maps/place/'+location_dig
      br.open(url)
      br.session.headers['User-Agent']
      br.select('span jstcache="182"')
      
      soup = BeautifulSoup(htmltext)
      searches = soup.findAll('div')
      print (searches)
      
      # geocode_result = gmaps.geocode(location)
      # re1 = '\'formatted_address\': \'([\w ,0-9\-]+)'
      # formatted_address = re.search(re1,str(geocode_result))
      # address = formatted_address.group(1)
      
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