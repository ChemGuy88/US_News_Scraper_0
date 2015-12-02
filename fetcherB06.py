#!/user/bin/python

# vB05. Successful script.
#
# Successfully scrapes address for search items using just BS. Un-
# fortunately google does not return an encased address for all search
# items. I can try searching a different html element, or go back to
# the v05, which will use selenium to read JS from GoogleMaps.
#
#

import os
import re
import sys
import urllib.request
from bs4 import BeautifulSoup
import time
import datetime

n = '\n'

f = open(r'c:\users\herman\gpe\usnews\htmlghp-all.txt', 'w')

protourl = r'https://www.google.com/search?q=address+for+'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
headers = { 'User-Agent' : user_agent }
ts = time.time() #timestamp
time_string = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

""" Address Fetcher
By Herman. Fetches address for universities.
"""

def main():
  file = sys.argv[1]
#  file = r'C:\users\herman\gpe\usnews\rankscs-sorted.txt'
  university_list_file = os.path.abspath(file)
  mark = university_list_file.find('.txt')
  protofile = university_list_file[:mark]
  suffix = '-addresses-ghp.txt'
  tofile = protofile + suffix
  error_log_file_name = protofile + '-errors-ghp.txt'
  error_log_file = open(error_log_file_name, 'w')
  university_list_data = open(university_list_file, 'r')
  proto_university_list = university_list_data.read().split('\n')
  university_list = []
  for item in proto_university_list:
    university_list.append(item.split(';'))
  for value in university_list:
    if len(value) < 4:
      del university_list[university_list.index(value)]
  university_list_data.close()
  newlist = []
  i = 1
  j = len(university_list)
  k = 0
#  print(j,'items to work through',n)
  for list in university_list:
#    if i == 4: #opt
#      writefile(tofile, newlist, k, error_log_file)
    try:
      print('Item',i,'of',j,n)
      location = '%s, %s' % (list[1], list[2])
      print(' ',location)
      location_as_url = location.replace(' ', '+')
      url = protourl+location_as_url
      req = urllib.request.Request(url,data=None, headers=headers)
      with urllib.request.urlopen(req) as request:
        html = request.read()
      soup = BeautifulSoup(html, 'html.parser')
      address = soup.find('div', class_='_eF').string
      print(' ',address,n)
      microlist = []
      for component in list:
        microlist.append(component)
      microlist.append(address)
      newlist.append(microlist)
    except Exception as e:
      error_time = time_string
      error_log = 'Error for '+location+' at '+error_time+n+str(e)+2*n
      error_log_file.write(error_log)
      microlist = []
      for component in list:
        microlist.append(component)
      microlist.append(location)
      newlist.append(microlist)
      k += 1
    i += 1
  writefile(tofile, newlist, k, error_log_file)
  
def writefile(tofile, newlist, k, error_log_file):
  time_stamp = time_string
  print ('There were',k,'errors.',n)
  if k < 1:
    error_log_file.write('No errors found on '+time_stamp)
  error_log_file.close()
  export_file = open(tofile, 'wb')
  print('Exporting new list to', tofile,n)
  for item in newlist:
    string = ';'.join(item)+n
    export_file.write(bytes(string, 'utf-8'))
  export_file.close()
  print('Done. Bye!')
  sys.exit(1)

if __name__ == '__main__':
  main()