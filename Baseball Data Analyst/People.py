import csv
#with open('baseballdatabank-master/core/People.csv') as csv_file
f = open('../People.sql', 'w')
f.write('insert into People')
csv_reader = csv.reader(open('../baseballdatabank-master/core/People.csv'), delimiter=',')
line_count = 0
row_count = sum(1 for row in csv_reader)
csv_reader = csv.reader(open('../baseballdatabank-master/core/People.csv'), delimiter=',')

for line_num, row in enumerate(csv_reader):

    if row_count-1!=line_num:
        ending = ','
    else:
        ending = ';'
        
    if line_num == 0:
        f.write(' values')
    else:
        f.write("\n(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)%s"%(f"'{row[0]}'", \
         f"'{row[1]}-{row[2]}-{row[3]}'" if not (''== row[1] or ''== row[2] or ''== row[3]) else "null",\
            "'"+row[4].replace("'","''")+"'" if not ''== row[4] else "null",\
            "'"+row[5].replace("'","''")+"'" if not ''== row[5] else "null",\
            "'"+row[6].replace("'","''")+"'" if not ''== row[6] else "null",\
            f"'{row[7]}-{row[8]}-{row[9]}'" if not (''== row[7] or ''== row[8] or ''== row[9]) else "null",\
            "'"+row[13].replace("'","''")+"'" if not ''== row[13] else "null",\
            "'"+row[14].replace("'","''")+"'" if not ''== row[14] else "null",\
            "'"+row[15].replace("'","''")+"'" if not ''== row[15] else "null",\
            f"{row[16]}" if not ''== row[16] else "null",\
            f"{row[17]}" if not ''== row[17] else "null",\
            f"'{row[18]}'" if not ''== row[18] else "null",\
            f"'{row[19]}'" if not ''== row[19] else "null",\
            f"'{row[20]}'" if not ''== row[20] else "null",\
            f"'{row[21]}'" if not ''== row[21] else "null", ending))
print(f'Processed {line_num} lines.')
f.close()
