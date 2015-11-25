#!/usr/bin/env python
# coding=utf-8

from os import listdir
from os.path import isfile, join

mypath = '.'

files = [f for f in listdir(mypath) if isfile(join(mypath,f))]

sets_data = list()
gets_data = list()

for f in files:
    data_file = open(f,"r")

    for l in data_file.readlines():
        l = l.strip()
        if l.endswith("Threads"):
            splited_l = l.split()
            sets_data.append(splited_l[0])
            sets_data.append(',')
            gets_data.append(splited_l[0])
            gets_data.append(',')
        if l.endswith("thread"):
            splited_l = l.split()
            sets_data.append(splited_l[0])
            sets_data.append(',')
            gets_data.append(splited_l[0])
            gets_data.append(',')
        if l.startswith("Sets"):
            splited_l = l.split()
            if splited_l[5].startswith("0.00"):
                print f
                del sets_data[-6:]
                del gets_data[-6:]
                continue
            sets_data.append(','.join([splited_l[1],splited_l[4],splited_l[5]]))
            sets_data.append("\n")
        if l.startswith("Gets"):
            splited_l = l.split()
            gets_data.append(','.join([w for w in splited_l if not w.startswith('G')]))
            gets_data.append("\n")
    data_file.close()

#print sets_data


f = open("set",'w')
f.writelines(sets_data)
f.close()

f = open("get",'w')
f.writelines(gets_data)
f.close()
