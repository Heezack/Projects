#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 19:57:20 2018

@author: zehe
"""

import csv
#with open('baseballdatabank-master/core/AwardsManagers.csv') as csv_file
f = open('../Managers.sql', 'w')
f.write('truncate table Managers;\n insert into Managers')
csv_reader = csv.reader(open('../baseballdatabank-master/core/Managers.csv'), delimiter=',')
line_count = 0
row_count = sum(1 for row in csv_reader)
csv_reader = csv.reader(open('../baseballdatabank-master/core/Managers.csv'), delimiter=',')

for line_num, row in enumerate(csv_reader):

    if row_count-1!=line_num:
        ending = ','
    else:
        ending = ';'
        
    if line_num == 0:
        f.write(' values')
    else:
        f.write("\n(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)%s"%(
            f"'{row[0]}'", \
            f"{row[1]}",\
            f"'{row[2]}'",\
            f"'{row[3]}'",\
            f"{row[4]}",\
            f"{row[5]}",\
            f"{row[6]}",\
            f"{row[7]}",\
            f"{row[8]}" if not ''==row[8] else 'null',\
            f"'{row[9]}'", ending))
print(f'Processed {line_num} lines.')
f.close()