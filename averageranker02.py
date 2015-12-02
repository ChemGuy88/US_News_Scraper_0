#!/user/bin/python

# gets ranks-sorted lists and creates a new list where the ranks are
# are averaged
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

def average_duplicates(list):
  temp_list = []
  for university in list:
    if university[1] not in index_maker(temp_list):
      temp_list.append(university)
    else:
      ranks_to_average = []
      ranks_to_average.append(university[0])
      ranks_to_average.append(get_rank(temp_list))
      ranks_as_nums = []
      for rank in ranks_to_average:
        ranks_as_nums.append(int(rank))
      average = mean(ranks_as_nums)
      university.pop(0)
      university.insert(0,average)

def get_rank(list):
  
      
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
  
def save_report(files,dir,loa):
  todir = os.path.dirname(os.path.abspath(dir))
  num_of_subjects = str(len(files))
  serial = '000'
  file_base = 'avgrank-report-'+num_of_subjects+'-'+serial+'.txt'
  file_name = os.path.join(todir,file_base)
  if os.path.exists(file_name):
    print('Report file exists. Overwriting',n)
  f = open(file_name,'w')
  f.write('Report for:'+n)
  for item in files:
    f.write(item+n)
  f.write(n+'Begin loa:'+n)
  for university in loa:
    f.write(';'.join(university)+n)
  f.close()
  
def check_backup(files, dir):
  dir_abspath = os.path.abspath(dir)
  dir = os.path.dirname(dir_abspath)
  filenames = os.listdir(dir)
  print(filenames,n)
  ## the following lines of code check 'filenames' to see
  ## if one of them is a backupfile.
  for filename in filenames:
    backup_file_match = re.search('avgranker-tmp-.*',filename)
    print('bfm:',backup_file_match,n)
    if backup_file_match:
      backup_file_name = backup_file_match[0]
      print('bfn:',backup_file_name,n)
      backup_file = os.path.join(dir,backup_file_name)
      print('backup file name:',backup_file,n)
      f = open(backup_file, 'r')
      backup_text = f.read()
      matches = re.findall('Backup file for:\n([. \\a-zA-Z\-0-9]*)\nBegin loa:',backup_text)
      list_of_backedup_files = matches[0].split(n)
      print(list_of_backedup_files,n)
      files_to_match = len(files)
      match_counter = 0
      for filename_in_backup_file in list_of_backedup_files:
        if filename_in_backup_file not in files:
          break
        else:
          match_counter += 1
      if files_to_match == match_counter:
        print ('found backup file!',n)
        sys.exit(1)
        extract_backup_file(backup_file_name)
    else:
      backup_result = 'false'
      backup_loa = []
      print('burestore failed')
      sys.exit(1)
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
    average_duplicates(list)
    print('  Printing rank list',k,'of',j,n)
    l = len(list)
    m = 1
    i = 0
    for list_of_university_details in list:
      university_name = get_university_super(i,list,'name')
      print('    Processing school',m,'of',l,',',university_name)
      microlist = []
      if university_name not in index_maker(loa):
        print('      Inserting',university_name,'for the first time in \'loa\'')
        for thing in get_university_super(i,list,'details'):
          microlist.append(thing)
        microlist.append(get_university_super(i,list,'rank'))
        i += 1
        loa.append(microlist)
        print(microlist,n)
      else:
        print('     ',university_name,'is already in \'loa\'; appending new rank.')
        insert_rank(loa,list_of_university_details,university_name)
        i += 1
      m += 1
    k += 1
  print('Saving work thus far.',n)
  save_file(files, loa, dir)
  return loa
  
def loa_sort_by_rank(university):
  return int(university[0])
  
def average_calculator(loa,num_of_subjects):
  for university in loa:
    print('raw',university)
    ranks = university[4:]
    print('  ranks',ranks)
    ranks_a = university[4:]
    print('  ranks_a',ranks_a)
    while len(ranks_a) < num_of_subjects:
      ranks_a.append('NA')
    print('  ranks_a NA',ranks_a)
    ranks_as_nums = []
    for rank in ranks:
      ranks_as_nums.append(int(rank))
    print('  ranks as nums',ranks_as_nums)
    average = str(int(mean(ranks_as_nums)))
    print('  mean',average)
    del university[4:]
    print('  snipped uni',university)
    university.insert(0,average)
    print('  uni w mean',university)
    for num in sorted(ranks_a, reverse=True):
      university.insert(1,num)
    print('  final uni',university,n)
  loa = sorted(loa,key=loa_sort_by_rank)
  return loa
  
def main():
  files = sys.argv[1:]
  dir = sys.argv[0]
  num_of_subjects = len(files)
  # loa, polygraph = check_backup(files, dir)
  # if polygraph == 'true':
    # print ('Found previously saved file:',n)
  # if polygraph == 'false':
    # print ('No backup found',n)
  loa = loa_maker(files, dir)
  sys.exit(1)
  loa = average_calculator(loa,num_of_subjects)
  save_report(files,dir,loa)

if __name__ == '__main__':
  main()