#!/usr/bin/python

import os
import re
import sys
import urllib

n = '\n'

"""US News Scraper
"""

def extract_ranks(html_file):
  print ('extracting ranks from html files...',n)
  file = open(html_file, 'r')
  file_text = file.read()
  print ('html file ready for reading',n)
  re1 = '<sup>#</sup>(\d\d?<sup>[\.\s]*)'
  re2 = '<p class="location">([A-Za-z\- &.,]+)\n*</p>'
  #stuck here; can't get res to search for '[.\n]+' which I need
  # to make re1 and re2, etc., be together. It's not taking the '\n'
  # inside the brackets
  matches = re.findall(re1, file_text)
  print ('printing matches',n)
  for match in matches:
    print (match)

def main():
  print ('welcome to the usnews scraper!',n)
  html_files = sys.argv[1:]
  for html_file in html_files:
    extract_ranks(html_file)
  
  sys.exit(1)

if __name__ == '__main__':
  main()
