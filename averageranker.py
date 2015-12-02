#!/user/bin/python

# gets ranks-sorted lists and creates a new list where the ranks are
# are average
#

import os
import sys
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
  print('      These universities are already in \'loa\':',indeces,n)
  return indeces
  
def insert_rank(loa,rank,university_name):
  thing_counter = -1
  for thing in loa:
    thing_counter += 1
    if university_name in thing:
      break
  print('thing counter:',thing_counter,n)
  if len(loa) > 1:
    microlist = loa[thing_counter]
  else:
    microlist = []
  microlist.append(rank)
  loa.pop(thing_counter)
  loa.insert(thing_counter,microlist)
  
def save_file(files):
  file = files[0]
  file_dir = os.path.dirname(file)
  file_base = os.path.basename(file)
  file_name = file_dir+'avgranker-tmp-'+file_base
  g = open(file_name,'w')
  g.write('Backup file for:'+n)
  g.write(files)
  g.write(n+'Begin loa:'+n)
  for university in loa:
    g.write(university.join(';')+n)
  g.close
  #########################
  ### add files to first line of save file so check_backup()
  ### can see what files were used for that run.
  
def check_backup(files):
  filenames = []
  for file in files:
    extracted_files = os.listdir(os.path.dirname(file))
    for i in extract_files:
      if i not in filenames:
        filesnames.append(i)
  for filename in filenames:
    backup_file = re.search('avgranker-tmp-',filename)
    if backup_file:
      backup_file_name = backup_file.group()
      f = open(backup_file_name, 'r')
      backup_text = f.read()
      files_check = re.findall('Backup file for:\n(.+\n)?(Begin loa:){1}
      files_check_list = files_check.group()
      # check file to see if files is same as files in file.
  

  
def main():
  files = sys.argv[1:]
  check_backup(files)
  lol = []
  for file in files:
    lol.append(get_lists(file))
  print('lol:',n,lol,n)
  loa = []
  j = len(lol)
  k = 1
  for list in lol:
    print('  Printing rank list',k,'of',j,n,list,n)
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
        insert_rank(loa,microlist,university_name)
        i += 1
      print('    Microlist ready for appending to \'loa\'. This is what will be appended:',2*n,microlist,n)
      m += 1
    k += 1
  print('Saving work thus far.',n)
  save_file(files)
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