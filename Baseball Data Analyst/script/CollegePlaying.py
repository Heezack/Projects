#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:50:41 2018

@author: zehe
"""

import csv
#with open('baseballdatabank-master/core/CollegePlaying.csv') as csv_file
f = open('../CollegePlaying.sql', 'w')
f.write('truncate table CollegePlaying;\n insert into CollegePlaying')
csv_reader = csv.reader(open('../baseballdatabank-master/core/CollegePlaying.csv'), delimiter=',')
line_count = 0
row_count = sum(1 for row in csv_reader)
csv_reader = csv.reader(open('../baseballdatabank-master/core/CollegePlaying.csv'), delimiter=',')

for line_num, row in enumerate(csv_reader):

    if row_count-1!=line_num:
        ending = ','
    else:
        ending = ';'
        
    if line_num == 0:
        f.write(' values')
    else:
        f.write("\n(%s,%s,%s)%s"%(
            f"'{row[0]}'", \
            f"'{row[1]}'", \
            f"{row[2]}",ending))

f.write('\n delete from collegePlaying where schoolID in (\'ctpostu\',\'txutper\',\'caallia\',\'txrange\');')

f.write('\n ALTER TABLE CollegePlaying ADD CONSTRAINT CollegePlaying_Fkey_schoolID FOREIGN KEY (schoolID) REFERENCES schools(schoolID)')
print(f'Processed {line_num} lines.')
f.close()