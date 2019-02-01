import csv
#with open('baseballdatabank-master/core/People.csv') as csv_file
f = open('../Salaries.sql', 'w')
f.write('insert into Salaries')
csv_reader = csv.reader(open('../baseballdatabank-master/core/Salaries.csv'), delimiter=',')
line_count = 0
row_count = sum(1 for row in csv_reader)
csv_reader = csv.reader(open('../baseballdatabank-master/core/Salaries.csv'), delimiter=',')

for line_num, row in enumerate(csv_reader):

    if row_count-1!=line_num:
        ending = ','
    else:
        ending = ';'
        
    if line_num == 0:
        f.write(' values')
    else:
        f.write("\n(%s,%s,%s,%s,%s)%s"%(\
        f"{row[0]}", \
            "'"+row[1].replace("'","''")+"'" if not ''== row[1] else "null",\
            "'"+row[2].replace("'","''")+"'" if not ''== row[2] else "null",\
            "'"+row[3].replace("'","''")+"'" if not ''== row[3] else "null",\
            f"'{row[4]}'",\
            ending))
print(f'Processed {line_num} lines.')
f.close()
