from os import listdir
from os.path import isfile, join
from os import system

mypath = '.'

files = [f for f in listdir(mypath) if isfile(join(mypath,f))]

for f in files:
    if (f.startswith('1')):
        fname_split = f.split(':')
        new_fname = fname_split[0]+'_'+fname_split[1]
        print new_fname
        rename_cmd = "mv "+ f+ ' '+new_fname
        system(rename_cmd )
    else:
        continue

