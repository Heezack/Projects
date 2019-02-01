#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:25:42 2018

@author: zehe
"""

import csv
#with open('baseballdatabank-master/core/Schools.csv') as csv_file
f = open('../Schools.sql', 'w')
f.write('truncate table Schools CASCADE;\n insert into Schools')
csv_reader = csv.reader(open('../baseballdatabank-master/core/Schools.csv'), delimiter=',')
line_count = 0
row_count = sum(1 for row in csv_reader)
csv_reader = csv.reader(open('../baseballdatabank-master/core/Schools.csv'), delimiter=',')

for line_num, row in enumerate(csv_reader):

    if row_count-1!=line_num:
        ending = ','
    else:
        ending = ';'
        
    if line_num == 0:
        f.write(' values')
    else:
        f.write("\n(%s,%s,%s,%s,%s)%s"%(
            f"'{row[0]}'", \
            "'"+row[1].replace("'","''")+"'",\
            "'"+row[2].replace("'","''")+"'",\
            f"'{row[3]}'",\
            f"'{row[4]}'", ending))
print(f'Processed {line_num} lines.')
f.close()