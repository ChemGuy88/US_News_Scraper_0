#!/user/bin/python
# Info from http://www.gregreda.com/2013/04/29/more-web-scraping-with-python/
# Trying to use different methods. Getting a 400(?) error which is a 
# bad request error, possibly because website detects I'm not coming
# from a browser. that's what headers are for.

import os
import re
import sys
import urllib
import requests
import googlemaps
import webbrowser

headers =(
{
 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/37.0.2049.0 Safari/537.36'
 })

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
      url = 'https://www.google.com/maps/place/'+location
      r = requests.get(url, headers=headers)
      print (r,n)
      print (r.headers,n)
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