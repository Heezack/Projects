import csv
#with open('baseballdatabank-master/core/People.csv') as csv_file
f = open('../Batting.sql', 'w')
f.write('insert into Batting')
csv_reader = csv.reader(open('../baseballdatabank-master/core/Batting.csv'), delimiter=',')
line_count = 0
row_count = sum(1 for row in csv_reader)
csv_reader = csv.reader(open('../baseballdatabank-master/core/Batting.csv'), delimiter=',')

for line_num, row in enumerate(csv_reader):

    if row_count-1!=line_num:
        ending = ','
    else:
        ending = ';'
        
    if line_num == 0:
        f.write(' values')
    else:
        f.write("\n(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)%s"%(\
            "'"+row[0].replace("'","''")+"'",\
            f"{row[1]}" if not '' == row[1] else "null",\
            f"{row[2]}" if not '' == row[2] else "null",\
            "'"+row[3].replace("'","''")+"'",\
            "'"+row[4].replace("'","''")+"'" ,\
            f"{row[5]}" if not '' == row[5] else "null",\
            f"{row[6]}" if not '' == row[6] else "null",\
            f"{row[7]}" if not '' == row[7] else "null",\
            f"{row[8]}" if not '' == row[8] else "null",\
            f"{row[9]}" if not '' == row[9] else "null",\
            f"{row[10]}" if not '' == row[10] else "null",\
            f"{row[11]}" if not '' == row[11] else "null",\
            f"{row[12]}" if not '' == row[12] else "null",\
            f"{row[13]}" if not '' == row[13] else "null",\
            f"{row[14]}" if not '' == row[14] else "null",\
            f"{row[15]}" if not '' == row[15] else "null",\
            f"{row[16]}" if not '' == row[16] else "null",\
            "'"+row[17].replace("'","''")+"'",\
            "'"+row[18].replace("'","''")+"'",\
            "'"+row[19].replace("'","''")+"'",\
            "'"+row[20].replace("'","''")+"'",\
            "'"+row[21].replace("'","''")+"'",\
            ending))
print(f'Processed {line_num} lines.')
f.close()
