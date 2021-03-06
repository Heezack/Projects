#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 18:38:53 2018

@author: zehe
"""

import csv
#with open('baseballdatabank-master/core/AwardsManagers.csv') as csv_file
f = open('../AwardsManagers.sql', 'w')
f.write('truncate table AwardsManagers;\n insert into AwardsManagers')
csv_reader = csv.reader(open('../baseballdatabank-master/core/AwardsManagers.csv'), delimiter=',')
line_count = 0
row_count = sum(1 for row in csv_reader)
csv_reader = csv.reader(open('../baseballdatabank-master/core/AwardsManagers.csv'), delimiter=',')

for line_num, row in enumerate(csv_reader):

    if row_count-1!=line_num:
        ending = ','
    else:
        ending = ';'
        
    if line_num == 0:
        f.write(' values')
    else:
        f.write("\n(%s,%s,%s,%s,%s,%s)%s"%(
            f"'{row[0]}'", \
            f"'{row[1]}'",\
            f"{row[2]}",\
            f"'{row[3]}'",\
            f"'{row[4]}'" if 'Y'== row[4] else "'N'",\
            f"'{row[5]}'" if not ''== row[5] else "null", ending))
print(f'Processed {line_num} lines.')
f.close()
