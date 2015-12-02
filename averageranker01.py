#!/user/bin/python

# gets ranks-sorted lists and creates a new list where the ranks are
# are average
#

import os
import sys
import re
from statistics import mean

n = '\n'

def get_lists(file):
  file_path = os.path.abspath(file)
  f = open(file_path, 'r')
  text = f.read()
  alpha_list = text.split('\n')
  list = []
  for thing in alpha_list:
    begotten_list = thing.split(';')
    if len(begotten_list) < 2:
      continue
    else:
      list.append(begotten_list)
  return list

def get_university_super(i,list,range_option):
  university_details_list = list[i]
  if range_option == 'name':
    university_details_result = university_details_list[1]
  if range_option == 'details':
    university_details_result = university_details_list[1:]
  if range_option == 'rank':
    university_details_result = university_details_list[0]
  return university_details_result
  
def index_maker(list):
  indeces = []
  for thing in list:
    indeces.append(thing[0])
  return indeces
  
def insert_rank(loa,list_of_university_details,university_name):
  rank = list_of_university_details[0]
  thing_counter = -1
  for thing in loa:
    thing_counter += 1
    if university_name in thing:
      break
  if len(loa) > 1:
    microlist = loa[thing_counter]
  else:
    print('else',n)
    microlist = []
  microlist.append(rank)
  loa.pop(thing_counter)
  loa.insert(thing_counter,microlist)
  
def save_file(files, loa, dir):
  file = files[0]
  todir = os.path.dirname(os.path.abspath(dir))
  serial = '000'
  file_base = 'avgranker-tmp-'+serial+'.txt'
  file_name = os.path.join(todir,file_base)
  if os.path.exists(file_name):
    print('Backup file exists. Overwriting',n)
  g = open(file_name,'w')
  g.write('Backup file for:'+n)
  for item in files:
    g.write(item+n)
  g.write(n+'Begin loa:'+n)
  for university in loa:
    g.write(';'.join(university)+n)
  g.close
  
def check_backup(dir):
  filenames = []
  ## 'filesnames' gives a list of all files in the directories
  ## from where the script was run from.
  for file in files:
    extracted_files = os.listdir(os.path.dirname(file))
    for i in extracted_files:
      if i not in filenames:
        filenames.append(i)
  ## the following lines of code check 'filenames' to see
  ## if one of them is a backupfile.
  for filename in filenames:
    backup_file_name = 0
    while backup_file_name == 0:
      backup_file = re.search('\w*avgranker-tmp-\w*',filename)
      if backup_file:
        backup_file_name = backup_file.group()
        print('backup file name:',backup_file_name,n)
        f = open(backup_file_name, 'r')
        backup_text = f.read()
        files_check = re.findall('Backup file for:\n(.+\n{1})+(Begin loa:){1}',backup_text)
        files_check_list = files_check.group()
        print(files_check_list,n)
        files_to_match = len(files)
        match_counter = 0
        for filename_in_backup_file in files_check_list:
          if filename_in_backup_file not in files:
            break
          else:
            match_counter += 1
        if files_to_match == match_counter:
          print ('found backup file!',n)
          extract_backup_file(backup_file_name)
      else:
        backup_result = 'false'
        backup_loa = []
        return (backup_loa, backup_result)
        
def extract_backup_file(backup_file_name):
  f = open(backup_file_name,'r')
  text = f.read()
  premark = text.find('Begin loa:')
  mark = premark+10
  text_tobe_read = text[mark:]
  alphatext = text_tobe_read.split('\n')
  loa = []
  for thing in alphatext:
    loa.append(thing.split(';'))
  backup_result = 'true'
  return (backup_loa, backup_result)
  
def loa_maker(files, dir):
  lol = []
  for file in files:
    lol.append(get_lists(file))
  loa = []
  j = len(lol)
  k = 1
  for list in lol:
    print('  Printing rank list',k,'of',j,n)
    l = len(list)
    m = 1
    i = 0
    for list_of_university_details in list:
      print('    Digesting university list',m,'of',l)
      print('    This is the raw data:',n,'  ',list_of_university_details,n)
      microlist = []
      university_name = get_university_super(i,list,'name')
      if university_name not in index_maker(loa):
        print('      Inserting',university_name,'for the first time in \'loa\'',n)
        for thing in get_university_super(i,list,'details'):
          microlist.append(thing)
        microlist.append(get_university_super(i,list,'rank'))
        i += 1
        loa.append(microlist)
      else:
        print('     ',university_name,'is already in \'loa\'; appending new rank.',n)
        insert_rank(loa,list_of_university_details,university_name)
        i += 1
      m += 1
    k += 1
  print('Saving work thus far.',n)
  save_file(files, loa, dir)
  return loa
  
def main():
  files = sys.argv[1:]
  dir = sys.argv[0]
  loa, polygraph = check_backup(dir)
  if polygraph == 'true':
    print ('Found previously saved file:',n)
  if polygraph == 'false':
    print ('No backup found',n)
    loa = loa_maker(files, dir)
  else:
    print ('Error, \'check_backup\' failed',n)
    sys.exit(1)
  for university in loa:
    average = mean(university[4:])
    del university[4:]
    university.append(average)
  proto_file_name = str(os.path.abspath(files[0]))
  file_name = proto_file_name[:proto_file_name.find('.txt')]
  save_name = file_name+'-avgrank.txt'
  f = open(save_name, 'w')
  for item in loa:
    f.write(';'.join(item)+'\n')
  f.close

if __name__ == '__main__':
  main()